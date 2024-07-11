from robots.abstract_robot import AbstractRobot
from robots.pose import Pose
from robots.joint import Joint


def check_connection(func):
    def wrapper(self, *args, **kwargs):
        if self.connected:
            return func(self, *args, **kwargs)
        else:
            raise ConnectionError('The robot is not connected.')
    return wrapper


def check_faultstate(func):
    def wrapper(self, *args, **kwargs):
        if self.fault_state:
            raise SystemError('The robot is in fault state.')
        else:
            return func(self, *args, **kwargs)
    return wrapper


class IRobot(AbstractRobot):

    @property
    def connected(self) -> bool:
        return self.__connected

    @property
    def grip_closed(self) -> bool:
        return self.__gripclosed

    @property
    def pose(self) -> Pose:
        return self.__pose

    @pose.setter
    def pose(self, new_pose: Pose) -> None:
        self.__pose = new_pose

    @property
    def joint(self) -> Joint:
        return self.__joint

    @joint.setter
    def joint(self, new_joint: Joint) -> None:
        self.__joint = new_joint

    @property
    def fault_state(self) -> bool:
        return self.__fault

    def __init__(self) -> None:
        self.__connected = False
        self.__gripclosed = False
        self.__pose = None
        self.__joint = None
        self.__fault = False
        print('Robô Kinova ligado e esperando conexão.')

    def connect(self) -> None:
        self.__connected = True

    @check_connection
    def disconnect(self) -> None:
        if self.connected:
            self.__connected = False

    @check_connection
    @check_faultstate
    def cartesian_move(self, pose: Pose) -> None:
        self.__pose = pose

    @check_connection
    @check_faultstate
    def joint_move(self, joint: Joint) -> None:
        self.__joint = joint

    @check_connection
    @check_faultstate
    def open_tool(self, actuation_time: float = 2) -> bool:
        if self.grip_closed:
            self.__gripclosed = False

    @check_connection
    @check_faultstate
    def close_tool(self, actuation_time: float = 2) -> bool:
        if not self.grip_closed:
            self.__gripclosed = True

    @check_connection
    def get_cartesian(self) -> list[float]:
        return self.pose.to_list

    @check_connection
    def get_joints(self) -> list[float]:
        return self.joint.to_list

    def _apply_emergency_stop(self) -> None:
        self.__fault = True

    @check_connection
    def _clear_fault(self) -> bool:
        if self.fault_state:
            self.__fault = False
            return True
        else:
            return False
