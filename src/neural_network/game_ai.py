from typing import List, Tuple
from game.checkers import Checkers
from game.board import Board, Coordinates
from game.piece import Piece
from game.pawn import Pawn
from game.queen import Queen
from neural_network.coords_parser import DetectionPiece, PieceType


class GameAI:

    adjascent_squares = {
        'a1': ['b2'],
        'a3': ['b2', 'b4'],
        'a5': ['b4', 'b6'],
        'a7': ['b6', 'b8'],
        'b2': ['a1', 'a3', 'c1', 'c3'],
        'b4': ['a3', 'a5', 'c3', 'c5'],
        'b6': ['a5', 'a7', 'c5', 'c7'],
        'b8': ['a7', 'c7'],
        'c1': ['b2', 'd2'],
        'c3': ['b2', 'b4', 'd2', 'd4'],
        'c5': ['b4', 'b6', 'd4', 'd6'],
        'c7': ['b6', 'b8', 'd6', 'd8'],
        'd2': ['c1', 'c3', 'e1', 'e3'],
        'd4': ['c3', 'c5', 'e3', 'e5'],
        'd6': ['c5', 'c7', 'e5', 'e7'],
        'd8': ['c7', 'e7'],
        'e1': ['d2', 'f2'],
        'e3': ['d2', 'd4', 'f2', 'f4'],
        'e5': ['d4', 'd6', 'f4', 'f6'],
        'e7': ['d6', 'd8', 'f6', 'f8'],
        'f2': ['e1', 'e3', 'g1', 'g3'],
        'f4': ['e3', 'e5', 'g3', 'g5'],
        'f6': ['e5', 'e7', 'g5', 'g7'],
        'f8': ['e7', 'g7'],
        'g1': ['f2', 'h2'],
        'g3': ['f2', 'f4', 'h2', 'h4'],
        'g5': ['f4', 'f6', 'h4', 'h6'],
        'g7': ['f6', 'f8', 'h6', 'h8'],
        'h2': ['g1', 'g3'],
        'h4': ['g3', 'g5'],
        'h6': ['g5', 'g7'],
        'h8': ['g7'],
    }

    board_as_int = {
        0: ('h1', False), 1: ('g1', True),
        2: ('f1', False), 3: ('e1', True),
        4: ('d1', False), 5: ('c1', True),
        6: ('b1', False), 7: ('a1', True),
        8: ('h2', True),  9: ('g2', False),
        10: ('f2', True), 11: ('e2', False),
        12: ('d2', True), 13: ('c2', False),
        14: ('b2', True), 15: ('a2', False),
        16: ('h3', False), 17: ('g3', True),
        18: ('f3', False), 19: ('e3', True),
        20: ('d3', False), 21: ('c3', True),
        22: ('b3', False), 23: ('a3', True),
        24: ('h4', True), 25: ('g4', False),
        26: ('f4', True), 27: ('e4', False),
        28: ('d4', True), 29: ('c4', False),
        30: ('b4', True), 31: ('a4', False),
        32: ('h5', False), 33: ('g5', True),
        34: ('f5', False), 35: ('e5', True),
        36: ('d5', False), 37: ('c5', True),
        38: ('b5', False), 39: ('a5', True),
        40: ('h6', True), 41: ('g6', False),
        42: ('f6', True), 43: ('e6', False),
        44: ('d6', True), 45: ('c6', False),
        46: ('b6', True), 47: ('a6', False),
        48: ('h7', False), 49: ('g7', True),
        50: ('f7', False), 51: ('e7', True),
        52: ('d7', False), 53: ('c7', True),
        54: ('b7', False), 55: ('a7', True),
        56: ('h8', True), 57: ('g8', False),
        58: ('f8', True), 59: ('e8', False),
        60: ('d8', True), 61: ('c8', False),
        62: ('b8', True), 63: ('a8', False),
    }

    def __init__(
            self,
            robot: str,
            adv: str,
            max_depth: int = 3,
    ) -> None:
        self.__robotcolor = robot
        self.__advcolor = adv
        self.__max_depth = max_depth

    @staticmethod
    def _square_to_int(square: str) -> int:
        for key, value in GameAI.board_as_int.items():
            if value[0] == square:
                return key

    @staticmethod
    def move_left(
            square: str,
            length: int,
            backwards: bool = False,
    ) -> List[str]:
        sqr = GameAI._square_to_int(square)
        available_moves = []
        i = length
        while i > 0:
            pos_key = None
            if backwards and sqr not in (7, 15, 23, 31, 39, 47, 55, 63):
                pos = sqr - 8 + 1
                pos_key, playble = GameAI.board_as_int[pos]
                if playble:
                    available_moves.append(pos_key)
            elif not backwards and sqr < 55 and sqr % 8 != 0:
                pos = sqr + 8 + 1
                pos_key, playble = GameAI.board_as_int[pos]
                if playble:
                    available_moves.append(pos_key)
            if pos_key is not None:
                sqr = GameAI._square_to_int(pos_key)
            i -= 1
        return available_moves

    @staticmethod
    def move_right(
            square: str,
            length: int,
            backwards: bool = False,
    ) -> List[str]:
        sqr = GameAI._square_to_int(square)
        available_moves = []
        i = length
        while i > 0:
            pos_key = None
            if backwards and sqr < 56 and (sqr + 1) % 8 != 0:
                pos = sqr - 8 - 1
                pos_key, playble = GameAI.board_as_int[pos]
                if playble:
                    available_moves.append(pos_key)
            elif not backwards and sqr < 55 and (sqr + 1) % 8 != 0:
                pos = sqr + 8 - 1
                pos_key, playble = GameAI.board_as_int[pos]
                if playble:
                    available_moves.append(pos_key)
            if pos_key is not None:
                sqr = GameAI._square_to_int(pos_key)
            i -= 1
        return available_moves

    def __validate_capture(
            self,
            board: Board,
            origin: str,
            target: str,
    ) -> bool:
        origin_coord = Coordinates(origin[0], int(origin[1]))
        target_coord = Coordinates(target[0], int(target[1]))
        return board._validate_capture(origin_coord, target_coord)

    def __get_queen_moves(
            self,
            board: Board,
            coordinates: Coordinates,
    ) -> Tuple[List[str], List[str]]:
        coords = f'{coordinates.col}{coordinates.row}'
        left_fwd = GameAI.move_left(coords, 7)
        right_fwd = GameAI.move_right(coords, 7)
        left_bwd = GameAI.move_left(coords, 7, True)
        right_bwd = GameAI.move_right(coords, 7, True)
        movements = []
        captures = []
        for move_list in [left_fwd, right_fwd, left_bwd, right_bwd]:
            maxidx = len(move_list) - 1
            i = 0
            _stop = False
            while i <= maxidx and not _stop:
                if board.is_empty(move_list[i]):
                    movements.append(move_list[i])
                else:
                    if i < maxidx and board.is_empty(move_list[i + 1]):
                        valid = self.__validate_capture(
                            board,
                            move_list[i],
                            move_list[i + 1],
                        )
                        if valid:
                            captures.append(move_list[i + 1])
                        else:
                            _stop = True
                    i += 1
                i += 1
        return (movements, captures)

    def __get_pawn_moves(
            self,
            board: Board,
            coordinates: Coordinates,
            endboard: bool = False,
    ) -> Tuple[List[str], List[str]]:
        coords = f'{coordinates.col}{coordinates.row}'
        left_fwd = GameAI.move_left(coords, 1, endboard)
        right_fwd = GameAI.move_right(coords, 1, endboard)
        movements = []
        captures = []
        for move_list in [left_fwd, right_fwd]:
            maxidx = len(move_list) - 1
            i = 0
            _stop = False
            while i <= maxidx and not _stop:
                if board.is_empty(move_list[i]):
                    movements.append(move_list[i])
                else:
                    if i < maxidx and board.is_empty(move_list[i + 1]):
                        valid = self.__validate_capture(
                            board,
                            move_list[i],
                            move_list[i + 1],
                        )
                        if valid:
                            captures.append(move_list[i + 1])
                        else:
                            _stop = True
                        i += 1
                i += 1
        return (movements, captures)

    def _eval_queen_capture(self, board: Board, piece: Queen):
        captures = self.__get_queen_moves(board, piece.coordinates)

    def _eval_capture(self, piece: Piece, captures: List[str]):
        if len(captures) == 0:
            return 0
        else:
            for capture in captures:
                # atribute a value for each capture
                pass

    def evaluate_moves(self, game: Checkers, robot: bool = True):
        board = game._board
        pieces = []
        inverted = self.__robotcolor != game._p1c
        print('Inverted: ', inverted)
        if robot:
            pieces = game._getpiece_by_color(self.__robotcolor)
        else:
            pieces = game._getpiece_by_color(self.__advcolor)
        for piece in pieces:
            moves = []
            captures = []
            if isinstance(piece, Queen):
                moves, captures = self.__get_queen_moves(
                    board,
                    piece.coordinates,
                )
            else:
                moves, captures = self.__get_pawn_moves(
                    board,
                    piece.coordinates,
                    inverted,
                )
            # In Priority Order:
            # 1. Capture
            # 1.1 Capture most pieces
            # 1.2 Capture most valuable pieces
            self._eval_capture(piece, captures)
            print(piece)
            print(moves)
            print(captures)
            # 2. Move
            # 2.1 Move to promote
            # 2.2 Move to capture
            # 2.3 Move defensively

    @staticmethod
    def filter_outerboard(
        pieces_list: List[DetectionPiece],
    ) -> List[DetectionPiece]:
        return [
            piece
            for piece in pieces_list
            if piece.coords.col in 'abcdefgh'
            and piece.coords.row in (1, 2, 3, 4, 5, 6, 7, 8)
        ]

    @staticmethod
    def detection_to_gamepieces(
            pieces_list: List[DetectionPiece],
            game: Checkers,
    ) -> List[Piece]:
        filtered_list = GameAI.filter_outerboard(pieces_list)
        pieces = [None] * len(filtered_list)
        i = 0
        for i in range(len(filtered_list)):
            p = filtered_list[i]
            if p.piece_type == PieceType.PAWN:
                new_piece = Pawn(
                    color=p.color,
                    coordinates=p.coords,
                    icon=game._geticon(p.color),
                    promote_row=game._getpromote(p.color),
                )
                pieces[i] = new_piece
            if p.piece_type == PieceType.QUEEN:
                new_piece = Queen(
                    color=p.color,
                    coordinates=p.coords,
                    icon=game._geticon(p.color, True),
                )
                pieces[i] = new_piece
        return pieces
