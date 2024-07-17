from abc import ABC, abstractmethod
from robots.pose import Pose
from robots.joint import Joint


class AbstractRobot(ABC):
    """Abstract robot class that
    represents a robot."""

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def cartesian_move(self, pose: Pose) -> None:
        raise NotImplementedError

    @abstractmethod
    def joint_move(self, joint: Joint) -> None:
        raise NotImplementedError

    @abstractmethod
    def open_tool(self, actuation_time: float = 2) -> bool:
        raise NotImplementedError

    @abstractmethod
    def close_tool(self, actuation_time: float = 2) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _apply_emergency_stop(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _clear_fault(self) -> bool:
        raise NotImplementedError
