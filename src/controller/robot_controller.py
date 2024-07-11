from robots.irobot import IRobot
from robots.pose import Pose
from robots.joint import Joint


class RobotController:

    @property
    def robot(self) -> IRobot:
        return self.__robot

    @property
    def move_map(self) -> dict[str, dict[str, float]]:
        return self.__movemap

    def __init__(
        self,
        robot: IRobot,
    ) -> None:
        self.__robot = robot
