from flask import Flask
from waitress import serve
from api.controllers.home_controller import home_controller
from api.controllers.robot_controller import robot_controller

from controller.robot_controller import RobotController
from robots.robot_enum import RobotEnum
from robots.kinova_robot import KinovaRobot
from robots.test_robot import TestRobot
from movebank.movebank import (
    MoveBank,
    RobotTableEnum,
)


class FlaskApp:

    def __init__(
        self,
        debug: bool = False,
        robot_type: RobotEnum = RobotEnum.KINOVA,
        table: RobotTableEnum = RobotTableEnum.KINOVA,
    ) -> None:
        self.__app = Flask(__name__)
        # a lot of things here
        self.__register_template()
        self.__register_blueprints()
        self.__robot_controller = self.__initiate_robot_controller(
            robot_type=robot_type,
            table=table,
        )
        if debug:
            self.debug_server()
        else:
            self.start_server()

    def __register_template(self) -> None:
        self.__app.static_folder = 'api/views/static'
        self.__app.template_folder = 'api/views/template'

    def __register_blueprints(self) -> None:
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
            cam_index = 1
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
