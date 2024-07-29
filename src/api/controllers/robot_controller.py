from flask import Blueprint, jsonify

robot_controller = Blueprint('robot_controller', __name__)


@robot_controller.route('/', methods=['GET'])
def robot_methods():
    return jsonify({
        0: {
            'title': 'Test Positions',
            'route': '.../test_positions/<pos_key: str>',
            'http_method': 'GET',
            'description': 'Allows to test bank positions for the robot.'
        },
        1: {
            'title': 'GET Positions',
            'route': '.../get_positions/<pos_key: str>',
            'http_method': 'POST',
            'description': 'Requests the robot to save the key to the movebank.'
        },
        2: {
            'title': 'Move Pieces',
            'route': '.../move_pieces/<list_pos_key: list[str]>',
            'http_method': 'GET',
            'description': '''Moves the robot arm throught the board,
            grasping the piece at the first reference and releasing at the last.'''
        },
        3: {
            'title': 'Remove Piece',
            'route': '.../remove_piece/<pos_key: str>',
            'http_method': 'GET',
            'description': 'Requests the robot arm to remove a piece from the board.'
        },
        4: {
            'title': 'Place Queen',
            'route': '.../place_queen/<pos_key, queen: tuple[str, int]>',
            'http_method': 'GET',
            'description': 'Requests the robot arm to place a queen in the board.'
        },
        5: {
            'title': 'Capture Dataset Photos',
            'route': '.../dataset/<photos: int>',
            'http_method': 'GET',
            'description': 'Requests the robot to capture N photos for the dataset.'
        },
        6: {
            'title': 'Detect Board',
            'route': '.../detect',
            'http_method': 'GET',
            'description': 'Requests the robot to detect the actual board state.'
        },
    }), 200


@robot_controller.route('/detect', methods=['GET'])
def detect():
    pass
