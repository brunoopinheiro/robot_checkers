from robots.irobot import IRobot
from robots.pose import Pose
from robots.joint import Joint
from movebank.movebank import MoveBank
from enum import Enum


MIDDLE_MOVE_HEIGHT = 'middle_move_height'
UPPER_MOVE_HEIGHT = 'upper_movement_height'
UPPER_DROP = 'upper_drop_height'


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
        self.robot.open_tool()

    def to_upperboard(self) -> None:
        """Moves the robot to the Upper Board pose via joints"""
        upperboardjoints = self.move_map.get_joints(
            key=_RoboStates.UPPER_BOARD.value,
        )
        print('Voltando à visão do tabuleiro.')
        self.robot.joint_move(upperboardjoints)

    def check_valid_keys(self, *args) -> bool:
        try:
            for key in args:
                self.move_map.get_cartesian(key)
            return True
        except KeyError:
            return False

    def _move_z(self, z: float) -> None:
        basepose = self.robot.pose
        basepose.z = z
        self.robot.cartesian_move(basepose)

    def _move_x_y(self, x: float, y: float) -> None:
        basepose = self.robot.pose
        basepose.x = x
        basepose.y = y
        self.robot.cartesian_move(basepose)

    def _movejoint(self, joint: int, degrees: float) -> None:
        basejoint_dict = self.robot.joint.to_dict
        basejoint_dict[f'j{joint}'] = degrees
        joint_ = Joint(**basejoint_dict)
        self.robot.joint_move(joint_)

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

    def _to_upper_move(self, target: str) -> float:
        target_pose = self.move_map.get_cartesian(target)
        upper_move_pose = self.move_map.get_cartesian(MIDDLE_MOVE_HEIGHT)
        z = upper_move_pose.z
        target_pose.z = z
        self.robot.cartesian_move(target_pose)
        return z

    def drop_piece(self) -> None:
        print('Movendo peça para a caixa.')
        self._to_custom_pose(UPPER_MOVE_HEIGHT)
        self._to_custom_pose(UPPER_DROP)
        self.robot.open_tool(2)
        self.to_upperboard()

    def capture_piece(self, origin: str, targets: list[str]) -> None:
        for tgt in targets:
            self.move_map.get_cartesian(tgt)
        self.robot.close_tool(1)
        print('Iniciando Captura de Peças')
        print(f'Origem: {origin}')
        self.to_upperboard()
        z = self._to_upper_move(origin)
        origin_coord = self.move_map.get_cartesian(origin)
        self.robot.cartesian_move(origin_coord)
        self.robot.close_tool(actuation_time=0.5)
        for tgt in targets:
            self._move_z(z)
            print(f'Alvo: {tgt}')
            self._to_upper_move(tgt)
            tgt_coord = self.move_map.get_cartesian(tgt)
            self.robot.cartesian_move(tgt_coord)
        self.robot.open_tool(actuation_time=0.5)
        self._move_z(z)
        self.to_upperboard()
        self.robot.open_tool()

    def remove_piece_from_board(self, piece_location: str) -> None:
        print(f'Removendo Peça {piece_location} do tabuleiro.')
        self.robot.close_tool(1)
        self.to_upperboard()
        z = self._to_upper_move(piece_location)
        target_pose = self.move_map.get_cartesian(piece_location)
        self.robot.cartesian_move(target_pose)
        self.robot.close_tool(actuation_time=0.5)
        self._move_z(z)
        self.drop_piece()

    def _get_queen(self, queen: str) -> None:
        print(f'Buscando {queen}')
        self.robot.close_tool(1)
        self.to_upperboard()
        self._to_custom_pose(f'{queen}_pregrip')
        self._to_custom_coords(queen)
        self.robot.close_tool(0.5)
        print('Peça capturada')
        self._to_custom_pose(UPPER_MOVE_HEIGHT)

    def place_queen(
            self,
            target_location: str,
            queen: int,
    ) -> None:
        q_key = f'dama{queen}'
        self._get_queen(q_key)
        target = self.move_map.get_cartesian(target_location)
        self._move_x_y(
            x=target.x,
            y=target.y,
        )
        self.robot.cartesian_move(target)
        self.robot.open_tool(0.5)
        print('Dama colocada')
        self._to_upper_move(
            target=UPPER_MOVE_HEIGHT,
        )
        self.to_upperboard()
