from robots.irobot import IRobot
from movebank.movebank import MoveBank
from enum import Enum


class _RoboStates(Enum):
    UNDEFINED = 'undefined'
    HOME = 'home'
    UPPER_BOARD = 'upper_view'


class RobotController:

    @property
    def robot(self) -> IRobot:
        return self.__robot

    @property
    def move_map(self) -> MoveBank:
        return self.__movemap

    def __init__(
        self,
        robot: IRobot,
        movebank: MoveBank,
    ) -> None:
        self.__robot = robot
        self.__movemap = movebank
        self.__state: _RoboStates = _RoboStates.UNDEFINED

    def connect(self) -> None:
        """Stablishes the robot connection"""
        if self.robot.connected is False:
            self.robot.connect()

    def disconnect(self) -> None:
        """Disconnects the robot"""
        if self.robot.connected:
            self.robot.disconnect()

    def to_home(self) -> None:
        """Moves the robot to the Home pose via joints"""
        homejoints = self.move_map.get_joints(_RoboStates.HOME.value)
        self.robot.joint_move(homejoints)

    def to_upperboard(self) -> None:
        """Moves the robot to the Upper Board pose via joints"""
        upperboardjoints = self.move_map.get_joints(
            key=_RoboStates.UPPER_BOARD.value,
        )
        self.robot.joint_move(upperboardjoints)

    def _to_custom_pose(self, jointskey: str) -> None:
        custompose = self.move_map.get_joints(jointskey)
        self.robot.joint_move(custompose)

    def _to_custom_coords(self, posekey: str) -> None:
        custompose = self.move_map.get_cartesian(posekey)
        self.robot.cartesian_move(custompose)
