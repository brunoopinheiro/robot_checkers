from typing import Optional
from flask import Flask
from waitress import serve
from api.controllers.home_controller import construct_home_blueprint
from api.controllers.robot_controller import construct_robot_blueprint
from api.controllers.game_controller import construct_game_blueprint

from controller.robot_controller import RobotController
from robots.robot_enum import RobotEnum
from robots.kinova_robot import KinovaRobot
from robots.test_robot import TestRobot
from movebank.movebank import (
    MoveBank,
    RobotTableEnum,
)
from neural_network.model import Model
from game.checkers import Checkers


class FlaskApp:

    def __init__(
        self,
        debug: bool = False,
        robot_type: RobotEnum = RobotEnum.KINOVA,
        table: RobotTableEnum = RobotTableEnum.KINOVA,
    ) -> None:
        self.__app = Flask(__name__)
        self._robot_controller = self.__initiate_robot_controller(
            robot_type=robot_type,
            table=table,
        )
        self._model = Model()
        self._game: Optional[Checkers] = None
        self.__register_template()
        self.__register_blueprints(table)
        if debug:
            self.debug_server()
        else:
            self.start_server()

    def __register_template(self) -> None:
        self.__app.static_folder = 'views/static'
        self.__app.template_folder = 'views/template'

    def __register_blueprints(self, table) -> None:
        robot_controller = construct_robot_blueprint(
            self._robot_controller,
            self._model,
            table,
        )
        home_controller = construct_home_blueprint()
        game_controller = construct_game_blueprint(
            self._init_game,
            self._get_game_instance,
            self._end_game,
            self._robot_controller,
        )
        self.__app.register_blueprint(
            robot_controller,
            url_prefix='/robot',
        )
        self.__app.register_blueprint(
            game_controller,
            url_prefix='/game',
        )
        self.__app.register_blueprint(
            home_controller,
            url_prefix='/',
        )

    def __initiate_robot_controller(
            self,
            robot_type: RobotEnum,
            table: RobotTableEnum,
    ) -> RobotController:
        robot = None
        if robot_type == RobotEnum.KINOVA:
            robot = KinovaRobot()
        else:
            robot = TestRobot()
        return RobotController(
            robot=robot,
            movebank=MoveBank(table),
        )

    def _init_game(self, game_instance: Checkers) -> None:
        self._game = game_instance
        self._game.start_game()

    def _get_game_instance(self) -> Optional[Checkers]:
        if self._game is None:
            return None
        return self._game

    def _end_game(self) -> dict:
        winner = self._game.winner
        rounds = self._game.rounds

        results = {
            'Winner': f'{winner}',
            'Rounds': rounds,
            'players': {
                '1': {
                    'pieces_left': len(self._game.p1_pieces),
                    'queens': self._game.p1_queens,
                    'color': self._game.p1_pieces[0].color
                },
                '2': {
                    'pieces_left': len(self._game.p2_pieces),
                    'queens': self._game.p2_queens,
                    'color': self._game.p2_pieces[0].color
                }
            }
        }
        self._game = None
        return results

    def debug_server(self) -> None:
        self.__app.run(
            debug=True,
            host='0.0.0.0',
            port='5000',
        )

    def start_server(self) -> None:
        serve(
            self.__app,
            host='0.0.0.0',
            port='5000',
        )
