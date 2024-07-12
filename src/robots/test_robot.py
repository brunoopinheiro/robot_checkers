from robots.irobot import (
    IRobot,
    check_connection,
    check_faultstate,
)
from time import sleep
from robots.pose import Pose
from robots.joint import Joint


class TestRobot(IRobot):

    def __init__(self) -> None:
        super().__init__()
        print('Robô de Testes Ligado e esperando Conexão')

    def connect(self) -> None:
        print('ROBO_TESTE: Estabelecendo Conexão')
        sleep(0.5)
        super().connect()
        if self.connected is True:
            print('Conexão Estabelecida com Sucesso.')
        else:
            print('Falha ao Estabelecer Conexão.')

    @check_connection
    def disconnect(self) -> None:
        sleep(0.5)
        super().disconnect()
        if self.connected is False:
            print('Conexão Finalizada com Sucesso.')
        else:
            print('Falha Finalizando Conexão.')

    @check_connection
    @check_faultstate
    def cartesian_move(self, pose: Pose) -> None:
        print(f'CART MOVE: {pose.to_dict}')
        sleep(0.8)
        super().cartesian_move(pose)

    @check_connection
    @check_faultstate
    def joint_move(self, joint: Joint) -> None:
        print(f'JOINT MOVE: {joint.to_dict}')
        sleep(0.8)
        super().joint_move(joint)

    @check_connection
    @check_faultstate
    def open_tool(self, actuation_time: float = 1) -> bool:
        print('Abrindo Garra.')
        sleep(actuation_time)
        super().open_tool(actuation_time)

    @check_connection
    @check_faultstate
    def close_tool(self, actuation_time: float = 1) -> bool:
        print('Fechando Garra.')
        sleep(actuation_time)
        super().close_tool(actuation_time)

    @check_connection
    def get_cartesian(self) -> list[float]:
        sleep(0.25)
        print(f'POSE: {self.pose.to_list}')
        return super().get_cartesian()

    @check_connection
    def get_joints(self) -> list[float]:
        sleep(0.25)
        print(f'JOINTS: {self.joint.to_list}')
        return super().get_joints()

    @check_connection
    def _apply_emergency_stop(self) -> None:
        super()._apply_emergency_stop()
        print('Parada de Emergência. Robô em Estado de Falta.')

    @check_connection
    def _clear_fault(self) -> bool:
        self.fault_state = False
        print('Limpeza de Falta bem sucedida.')
