from robots.irobot import IRobot
from robots.pose import Pose
from robots.joint import Joint
from movebank.movebank import MoveBank
from enum import Enum


class _RoboStates(Enum):
    UNDEFINED = 'undefined'
    HOME = 'home'
    UPPER_BOARD = 'upper_view'


class RobotController:

    __instance = None

    @property
    def robot(self) -> IRobot:
        return self.__robot

    @property
    def move_map(self) -> MoveBank:
        return self.__movemap

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(
                RobotController,
                cls).__new__(cls)
        return cls.__instance

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

    def get_positions(self) -> tuple[Joint, Pose]:
        self.robot.get_joints()
        self.robot.get_cartesian()
        joints = self.robot.joint
        pose = self.robot.pose
        return (joints, pose)

    def record_position(self, pos_key: str) -> None:
        joints, pose = self.get_positions()
        self.move_map._record_positions(
            pos_key=pos_key,
            joint=joints,
            pose=pose,
        )

    def _to_custom_pose(self, jointskey: str) -> None:
        custompose = self.move_map.get_joints(jointskey)
        self.robot.joint_move(custompose)

    def _to_custom_coords(self, posekey: str) -> None:
        custompose = self.move_map.get_cartesian(posekey)
        self.robot.cartesian_move(custompose)
