from robots.irobot import (
    IRobot,
    check_connection,
    check_faultstate,
)
from robots.pose import Pose
from robots.joint import Joint
from rria_api.robot_object import RobotObject
from rria_api.robot_enum import RobotEnum


class KinovaRobot(IRobot):

    IP = '192.168.2.10'

    @property
    def kinova(self) -> RobotObject:
        return self.__kinova

    def __init__(self) -> None:
        super().__init__()
        self.__kinova = RobotObject(
            ip_address=KinovaRobot.IP,
            robot_type=RobotEnum.GEN3_LITE,
        )
        print('Robô Kinova ligado e esperando conexão.')

    def connect(self) -> None:
        print('KINOVA: Estabelecendo Conexão')
        self.kinova.connect_robot()
        super().connect()
        if self.connected is True:
            print('Conexão Estabelecida com Sucesso')
        else:
            print('Falha ao Estabelecer Conexão.')

    @check_connection
    def disconnect(self) -> None:
        self.kinova.safe_disconnect()
        super().disconnect()
        if self.connected is False:
            print('Conexão Finalizada com Sucesso')
        else:
            print('Falha Finalizando Conexão')

    @check_connection
    @check_faultstate
    def cartesian_move(self, pose: Pose) -> None:
        print(f'CART MOVE: {pose.to_list}')
        self.kinova.move_cartesian(**pose.to_dict)
        super().cartesian_move(pose)

    @check_connection
    @check_faultstate
    def joint_move(self, joint: Joint) -> None:
        print(f'JOINT MOVE: {joint.to_list}')
        self.kinova.move_joints(**joint.to_dict)
        super().joint_move(joint)

    @check_connection
    @check_faultstate
    def open_tool(self, actuation_time: float = 1) -> bool:
        print('Abrindo Garra')
        self.kinova.open_gripper(actuation_time)
        super().open_tool(actuation_time)

    @check_connection
    @check_faultstate
    def close_tool(self, actuation_time: float = 1) -> bool:
        print('Fechando Garra')
        self.kinova.close_gripper(actuation_time)
        super().close_tool(actuation_time)

    @check_connection
    def get_cartesian(self) -> list[float]:
        new_pose = self.kinova.get_cartesian()
        pose = Pose(*new_pose)
        self.pose = pose
        print(f'POSE: {self.pose.to_dict}')
        return pose.to_list

    @check_connection
    def get_joints(self) -> list[float]:
        new_joints = self.kinova.get_joints()
        joint = Joint(*new_joints)
        self.joint = joint
        print(f'JOINTS: {self.joint.to_dict}')
        return joint.to_list

    def _apply_emergency_stop(self) -> None:
        self.kinova.apply_emergency_stop()
        super()._apply_emergency_stop()
        print('Parada de Emergência. Robô em Estado de Falta.')

    @check_connection
    def _clear_fault(self) -> bool:
        print('Limpeza do Estado de Falta Ainda Não Implementada')
