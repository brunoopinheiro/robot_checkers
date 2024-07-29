from flask import Flask
from waitress import serve
from api.controllers.home_controller import construct_home_blueprint
from api.controllers.robot_controller import construct_robot_blueprint

from controller.robot_controller import RobotController
from robots.robot_enum import RobotEnum
from robots.kinova_robot import KinovaRobot
from robots.test_robot import TestRobot
from movebank.movebank import (
    MoveBank,
    RobotTableEnum,
)
from neural_network.model import Model


class FlaskApp:

    def __init__(
        self,
        debug: bool = False,
        robot_type: RobotEnum = RobotEnum.KINOVA,
        table: RobotTableEnum = RobotTableEnum.KINOVA,
    ) -> None:
        self.__app = Flask(__name__)
        # a lot of things here
        self._robot_controller = self.__initiate_robot_controller(
            robot_type=robot_type,
            table=table,
        )
        self._model = Model()
        self.__register_template()
        self.__register_blueprints()
        self._robot_controller.connect()
        if debug:
            self.debug_server()
        else:
            self.start_server()

    def __register_template(self) -> None:
        self.__app.static_folder = 'views/static'
        self.__app.template_folder = 'views/template'

    def __register_blueprints(self) -> None:
        robot_controller = construct_robot_blueprint(
            self._robot_controller,
            self._model,
        )
        home_controller = construct_home_blueprint()
        self.__app.register_blueprint(
            robot_controller,
            url_prefix='/robot',
        )
        self.__app.register_blueprint(
            home_controller,
            url_prefix='/',
        )

    def __initiate_robot_controller(
            self,
            robot_type: RobotEnum,
            table: RobotTableEnum,
            cam_index: int = 0,
    ) -> RobotController:
        robot = None
        if robot_type == RobotEnum.KINOVA:
            robot = KinovaRobot()
            cam_index = 0
        else:
            robot = TestRobot()
        return RobotController(
            robot=robot,
            movebank=MoveBank(table),
            cam_index=cam_index,
        )

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
