from robots.irobot import IRobot
from robots.pose import Pose
from robots.joint import Joint
from movebank.movebank import MoveBank
from enum import Enum


MIDDLE_MOVE_HEIGHT = 'middle_move_height'
UPPER_MOVE_HEIGHT = 'upper_movement_height'
UPPER_DROP = 'upper_drop_height'
QUEEN_STEP1 = 'queen_placement_middle'
QUEEN_STEP2 = 'queen_placement_row8'
UPPER_VIEW = 'upper_view_board'
SAFE_SHUTDOWN = 'safe_shutdown'


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

    def to_disconnect(self) -> None:
        joints_ = self.move_map.get_joints(
            key=SAFE_SHUTDOWN
        )
        self.robot.joint_move(joints_)

    def check_valid_keys(self, *args) -> bool:
        """Receives a variable number of map keys and checks
        if they all are valid keys."""
        try:
            for key in args:
                self.move_map.get_cartesian(key)
            return True
        except KeyError:
            return False

    def _move_z(self, z: float) -> None:
        """Moves the robot cartesianly only in the Z axis."""
        basepose = self.robot.pose
        basepose.z = z
        self.robot.cartesian_move(basepose)

    def _move_x_y(self, x: float, y: float) -> None:
        """Moves the robot cartesianly only in the X and Y axis."""
        basepose = self.robot.pose
        basepose.x = x
        basepose.y = y
        self.robot.cartesian_move(basepose)

    def _movejoint(self, joint: int, degrees: float) -> None:
        """Moves the robot by joints reference."""
        basejoint_dict = self.robot.joint.to_dict
        basejoint_dict[f'j{joint}'] = degrees
        joint_ = Joint(**basejoint_dict)
        self.robot.joint_move(joint_)

    def get_positions(self) -> tuple[Joint, Pose]:
        """Gets the actual robot pose and returns
        a tuple with its joints and cartesian references
        as `Joint` and `Pose` objects."""
        self.robot.get_joints()
        self.robot.get_cartesian()
        joints = self.robot.joint
        pose = self.robot.pose
        return (joints, pose)

    def record_position(self, pos_key: str) -> None:
        """Uses the `MoveMap` object instance to
        update the `.json` file with the movement keys."""
        joints, pose = self.get_positions()
        self.move_map._record_positions(
            pos_key=pos_key,
            joint=joints,
            pose=pose,
        )

    def _to_custom_pose(self, jointskey: str) -> None:
        """Moves the robot by joints reference to a custom
        position."""
        custompose = self.move_map.get_joints(jointskey)
        self.robot.joint_move(custompose)

    def _to_custom_coords(self, posekey: str) -> None:
        """Moves the robot by coordinates reference to
        a custom position."""
        custompose = self.move_map.get_cartesian(posekey)
        self.robot.cartesian_move(custompose)

    def _to_upper_move(self, target: str) -> float:
        """Moves the robot to the X and Y axis of a given
        target key, maintaining the Z axis from the
        `middle_movement_height` key."""
        target_pose = self.move_map.get_cartesian(target)
        upper_move_pose = self.move_map.get_cartesian(MIDDLE_MOVE_HEIGHT)
        z = upper_move_pose.z
        target_pose.z = z
        self.robot.cartesian_move(target_pose)
        return z

    def drop_piece(self) -> None:
        """Drops a piece in the drop box assuming the robot
        already has the piece grasped."""
        print('Movendo peça para a caixa.')
        self._to_custom_pose(UPPER_MOVE_HEIGHT)
        self._to_custom_pose(UPPER_DROP)
        self.robot.open_tool(2)
        self.to_upperboard()

    def capture_piece(self, origin: str, targets: list[str]) -> None:
        """Captures a variable number of pieces, from an origin point.
        This function does not remove pieces from the game board."""
        for tgt in targets:
            self.move_map.get_cartesian(tgt)
        print('Iniciando Captura de Peças')
        print(f'Origem: {origin}')
        # self.robot.close_tool()
        self.to_upperboard()
        z = self._to_upper_move(origin)
        origin_coord = self.move_map.get_cartesian(origin)
        self.robot.cartesian_move(origin_coord)
        self.robot.close_tool()
        for tgt in targets:
            self._move_z(z)
            print(f'Alvo: {tgt}')
            self._to_upper_move(tgt)
            tgt_coord = self.move_map.get_cartesian(tgt)
            self.robot.cartesian_move(tgt_coord)
        self.robot.open_tool()
        self._move_z(z)
        self.to_upperboard()
        self.robot.open_tool()

    def remove_piece_from_board(self, piece_location: str) -> None:
        """Removes a piece from the board, based on its key location."""
        print(f'Removendo Peça {piece_location} do tabuleiro.')
        # self.robot.close_tool()
        self.to_upperboard()
        z = self._to_upper_move(piece_location)
        target_pose = self.move_map.get_cartesian(piece_location)
        self.robot.cartesian_move(target_pose)
        self.robot.close_tool()
        self._move_z(z)
        self.drop_piece()

    def capture_and_remove(self, origin, jumps):
        size = len(jumps)
        targets = [None] * size
        dests = [None] * size
        for i in range(size):
            targets[i] = jumps[i][0]
            dests[i] = jumps[i][1]
        self.capture_piece(origin, dests)
        for tgt in targets:
            self.remove_piece_from_board(tgt)

    def _get_queen(self, queen: str) -> None:
        """Retrieves a queen and returns to the
        `upper_movement_height` position"""
        print(f'Buscando {queen}')
        # self.robot.close_tool()
        self.to_upperboard()
        self._to_custom_pose(f'{queen}_pregrip')
        self._to_custom_coords(queen)
        self.robot.close_tool()
        print('Peça capturada')
        self._move_z(0.05)
        self._to_custom_pose(QUEEN_STEP1)
        self._to_custom_coords(QUEEN_STEP1)

    def place_queen(
            self,
            target_location: str,
            queen: int,
    ) -> None:
        """Retrieves a queen and places in a target
        location key."""
        q_key = f'dama{queen}'
        self._get_queen(q_key)
        target = self.move_map.get_cartesian(target_location)
        self._move_x_y(
            x=target.x,
            y=target.y,
        )
        self.robot.cartesian_move(target)
        self.robot.open_tool()
        print('Dama colocada')
        self._move_z(0.1)
        self._to_custom_pose(QUEEN_STEP2)
        self.to_upperboard()
        self.robot.open_tool()
