from flask import Blueprint, jsonify, Response
from game.checkers import Checkers
from game.coordinates import Coordinates
from controller.robot_controller import RobotController
from capture.capture_module import CaptureModule
from neural_network.model import Model
from neural_network.game_ai import (
    GameAI,
    GameAIResult,
    GameAIResultType,
)

GAME_NOT_STARTED = {'404': 'Game not started.'}


def construct_game_blueprint(
        init_game_function,
        get_game_instance,
        eng_game_function,
        robotcontroller: RobotController,
        model: Model,
) -> Blueprint:

    game_controller = Blueprint('game_controller', __name__)

    def __getprotoboard():
        game_instance: Checkers = get_game_instance()
        if game_instance is None:
            return jsonify(GAME_NOT_STARTED), 404
        game_instance.board_state()
        protogame = game_instance.proto_board()
        return protogame

    @game_controller.before_request
    def connect_robot():
        robotcontroller.connect()
        robotcontroller.robot.open_tool()

    @game_controller.after_request
    def disconnect_robot(response):
        robotcontroller.to_disconnect()
        robotcontroller.disconnect()
        return response

    @game_controller.route('/help', methods=['GET'])
    def game_routes():
        return jsonify({
            0: {
                'title': 'Start Game',
                'route': '../start/<int:robot>/<p1_color>/<p2_color>',
                'http_method': 'GET',
                'desc': 'Starts a checkers game.',
            }
        })

    @game_controller.route(
            '/start/<int:first_player>/<human_color>/<robot_color>',
            methods=['GET'],
        )
    def start_game(
        first_player: int,
        human_color: str,
        robot_color: str,
    ):
        # convert to proto
        game_instance = get_game_instance()
        if game_instance is not None:
            return jsonify({'Error': 'Game already in progress'}), 400
        game = Checkers(
            first_player=first_player,
            human_color=human_color.lower(),
            robot_color=robot_color.lower(),
        )
        init_game_function(game)
        protogame = __getprotoboard()
        res = Response(bytes(protogame), status=200)
        return res

    @game_controller.route('/state')
    def game_state():
        protogame = __getprotoboard()
        res = Response(bytes(protogame), status=200)
        return res

    def __make_move(next_play: GameAIResult) -> bool:
        game: Checkers = get_game_instance()
        if next_play.play_type == GameAIResultType.CAPTURE:
            res = game.jump_multiple(
                next_play.origin,
                [(j.target, j.destiny) for j in next_play.jumps],
            )
            if res is True:
                origin = f'{next_play.origin.col}{next_play.origin.row}'
                jumps = []
                for j in next_play.jumps:
                    tgt = f'{j.target.col}{j.target.row}'
                    dt = f'{j.destiny.col}{j.destiny.row}'
                    jumps.append((tgt, dt))
                robotcontroller.capture_and_remove(origin, jumps=jumps)
                # this is not automatically placing a queen
                return True
        if next_play.play_type == GameAIResultType.MOVEMENT:
            res = game.move_piece(next_play.origin, next_play.destiny)
            if res is True:
                origin = f'{next_play.origin.col}{next_play.origin.row}'
                destiny = f'{next_play.destiny.col}{next_play.destiny.row}'
                robotcontroller.capture_piece(origin, [destiny])
                return True
        return False

    @game_controller.route('/robot_play', methods=['GET'])
    def robot_play():
        # go to upperview
        game_instance: Checkers = get_game_instance()
        if game_instance is None:
            return jsonify(GAME_NOT_STARTED), 404
        robotcontroller.to_upperboard()
        img = None
        count = 0
        cam_idx = 0
        table = robotcontroller.move_map.table
        if table == 2:
            cam_idx = 1
        capture_module = CaptureModule(cam_idx)
        camera_capt = True
        while img is None and count < 3:
            img = capture_module.capture_opencv()
            count += 1
            if count >= 2:
                camera_capt = False
                return jsonify({'Error', 'Could not capture a picture'}), 500
        capture_module.video_capture.release()
        # detect board, update board
        if camera_capt is True:
            predict_list = model.predict_from_opencv(img, table)
            # decide play
            pieces_list = GameAI.detection_to_gamepieces(
                predict_list,
                game_instance,
            )
            print(pieces_list)
            game_instance.overwrite_board(pieces_list)
        # play
        gameai = GameAI(
            robot=game_instance.robot_color,
            adv=game_instance.human_color,
        )
        next_play = gameai.evaluate_moves(game_instance)
        print(next_play)
        playres = __make_move(next_play)
        protogame = __getprotoboard()
        status = 0
        if playres is True:
            status = 200
        else:
            status = 500
        res = Response(bytes(protogame), status=status)
        return res

    @game_controller.route('/check_winner', methods=['GET'])
    def check_winner():
        game_instance: Checkers = get_game_instance()
        if game_instance is None:
            return jsonify(GAME_NOT_STARTED), 404
        if game_instance.is_finished:
            return jsonify({'winner': f'{game_instance.winner}'}), 200
        else:
            return jsonify({'winner': 'None'}), 204

    @game_controller.route('/move_piece/<origin>/<destiny>', methods=['GET'])
    def move_piece(origin, destiny):
        # convert to proto
        try:
            game_instance = get_game_instance()
            if game_instance is None:
                return jsonify(GAME_NOT_STARTED), 404
            origin_coord = Coordinates(
                col=origin[0],
                row=int(origin[1]),
            )
            destiny_coord = Coordinates(
                col=destiny[0],
                row=int(destiny[1]),
            )
            game_instance.move_piece(
                origin=origin_coord,
                destiny=destiny_coord,
            )
            return jsonify({'ok': 'Piece moved.'}), 200
        except Exception as err:
            return jsonify({'Error': f'{err}'}), 500

    @game_controller.route('/single_jump/<origin>/<target>/<destiny>')
    def single_jump(
        origin,
        target,
        destiny,
    ):
        # convert to proto
        # integrate with multi jump
        try:
            game_instance = get_game_instance()
            if game_instance is None:
                return jsonify(GAME_NOT_STARTED), 404
            origin_coord = Coordinates(
                origin[0],
                int(origin[1]),
            )
            target_coord = Coordinates(
                target[0],
                int(target[1]),
            )
            destiny_coord = Coordinates(
                destiny[0],
                int(destiny[1]),
            )
            game_instance.jump_piece(
                origin_coord,
                destiny_coord,
                target_coord,
            )
            return jsonify({'ok': 'Jump executed successfully.'}), 200
        except Exception as err:
            return jsonify({'Error': f'{err}'}), 500

    @game_controller.route('/end', methods=['GET'])
    def end_game():
        try:
            results = eng_game_function()
            return jsonify(results), 200
        except Exception as err:
            return jsonify({'Error': f'{err}'}), 500

    return game_controller
