from robots.irobot import IRobot


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
