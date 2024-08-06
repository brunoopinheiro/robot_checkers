from typing import List, Optional, Tuple
from game.checkers import Checkers
from game.board import Board, Coordinates
from game.piece import Piece
from game.pawn import Pawn
from game.queen import Queen
from neural_network.coords_parser import DetectionPiece, PieceType
from neural_network.results.game_ai_result import (
    GameAIResult,
    GameAIResultType,
    Jump,
)
from neural_network.capture_tree.tree import Tree, Node
from random import choice


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
    ) -> None:
        self.__robotcolor = robot
        self.__advcolor = adv
        self.captree: Optional[Tree] = None
        self.deepest_capt_value = 0
        self.deepest_capt: List[Node] = []

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

    def __capture_result(self) -> GameAIResult:
        origin_ref = self.deepest_capt[0].target
        origin = Coordinates(origin_ref[0], int(origin_ref[1]))
        size = (len(self.deepest_capt)-2)
        jumps = [None] * size
        i = 0
        while i < size:
            jump_node = self.deepest_capt[i+1]
            tgt = jump_node.target
            dt = jump_node.destiny
            target = Coordinates(tgt[0], int(tgt[1]))
            destiny = Coordinates(dt[0], int(dt[1]))
            jump = Jump(target, destiny)
            jumps[i] = jump
        return GameAIResult(
            play_type=GameAIResultType.CAPTURE,
            origin=origin,
            jumps=jumps,
            destiny=None
        )

    def __move_result(
            self,
            moves_list: List[Tuple[Piece, List[str]]],
    ) -> GameAIResult:
        piece, move_opts = choice(moves_list)
        move = choice(move_opts)
        return GameAIResult(
            play_type=GameAIResultType.MOVEMENT,
            origin=piece.coordinates,
            jumps=None,
            destiny=Coordinates(move[0], int(move[1]))
        )

    def __find_captures(
            self,
            board: Board,
            piece: Piece,
            origin_node: Optional[Node] = None,
    ) -> None:
        lgt = piece.jump_length
        print(f'Obtaining all movementes within {lgt} squares')
        coords = None
        if origin_node is None:
            coords = f'{piece.coordinates.col}{piece.coordinates.row}'
        else:
            coords = origin_node.destiny
        # dada uma posição inicial
        if self.captree is None:
            self.captree = Tree(coords)
        if origin_node is None:
            origin_node = self.captree.root
        # encontrar todas as peços inimigas em distânica de pulo
        left_fwd = GameAI.move_left(coords, lgt)
        right_fwd = GameAI.move_right(coords, lgt)
        left_bwd = GameAI.move_left(coords, lgt, True)
        right_bwd = GameAI.move_left(coords, lgt, True)
        # para cada peça inimiga em distância de pulo,
        print('2.2 - Got the Moves')
        print([left_fwd, right_fwd, left_bwd, right_bwd])
        for moves in [left_fwd, right_fwd, left_bwd, right_bwd]:
            print('2.3 - Checking Moves')
            print(moves)
            closest = None
            maxidx = len(moves) - 2
            print(maxidx)
            i = 0
            if len(moves) >= 2:
                while i <= maxidx and closest is None:
                    print('Moves I: ', i)
                    sqr = moves[i]
                    next_sqr = moves[i+1]
                    i += 1
                    tgt = Coordinates(sqr[0], int(sqr[1]))
                    dest = Coordinates(next_sqr[0], int(next_sqr[1]))
                    # verificar se há espaço em branco depois da peça
                    value = board._validate_capture(tgt, dest)
                    if value == 2:
                        # queen
                        closest = origin_node.append_child(sqr, next_sqr, True)
                    elif value == 1:
                        # pawn
                        closest = origin_node.append_child(sqr, next_sqr)
                # repetir até que não haja peça para pular ou espaço atrás
            if closest is not None:
                self.__find_captures(board, piece, closest)

    def __get_queen_moves(
            self,
            board: Board,
            piece: Queen,
    ) -> List[str]:
        coordinates = piece.coordinates
        coords = f'{coordinates.col}{coordinates.row}'
        left_fwd = GameAI.move_left(coords, 7)
        right_fwd = GameAI.move_right(coords, 7)
        left_bwd = GameAI.move_left(coords, 7, True)
        right_bwd = GameAI.move_right(coords, 7, True)
        movements = []
        for move_list in [left_fwd, right_fwd, left_bwd, right_bwd]:
            maxidx = len(move_list) - 1
            i = 0
            _stop = False
            while i <= maxidx and not _stop:
                if board.is_empty(move_list[i]):
                    movements.append(move_list[i])
                else:
                    _stop = True
                i += 1
        return movements

    def __get_pawn_moves(
            self,
            board: Board,
            piece: Pawn,
            endboard: bool = True,
    ) -> List[str]:
        coordinates = piece.coordinates
        coords = f'{coordinates.col}{coordinates.row}'
        left_fwd = GameAI.move_left(coords, 1, endboard)
        right_fwd = GameAI.move_right(coords, 1, endboard)
        movements = []
        print([left_fwd, right_fwd])
        print([left_fwd, right_fwd])
        for move_list in [left_fwd, right_fwd]:
            maxidx = len(move_list) - 1
            i = 0
            _stop = False
            while i <= maxidx and not _stop:
                if board.is_empty(move_list[i]):
                    movements.append(move_list[i])
                else:
                    _stop = True
                i += 1
        return movements

    def evaluate_moves(self, game: Checkers, robot: bool = True):
        board = game._board
        pieces = []
        if robot:
            pieces = game._getpiece_by_color(self.__robotcolor)
        else:
            pieces = game._getpiece_by_color(self.__advcolor)
        print('2 - Pieces Obtained')
        for piece in pieces:
            coords = f'{piece.coordinates.col}{piece.coordinates.row}'
            self.captree = Tree(coords)
            print('2.1 - Reseting Capture Tree')
            # In Priority Order:
            # 1. Capture
            # 1.1 Capture most pieces
            # 1.2 Capture most valuable pieces
            self.__find_captures(
                board,
                piece,
            )
            print('2.2 - Possible Captures calculated')
            deepest_node = self.captree.depth_search()
            if deepest_node.depth > self.deepest_capt_value:
                self.deepest_capt = self.captree.trace_back(deepest_node)
        if self.deepest_capt_value > 0:
            print('2.2.1 - Possible Capture found')
            return self.__capture_result()
        print('3 - No captures, calculating moves')
        all_moves = []
        for piece in pieces:
            # 2. Move
            print(piece)
            moves = []
            if isinstance(piece, Queen):
                print('3.1 - Calculating Queen Moves')
                moves = self.__get_queen_moves(
                    board,
                    piece,
                )
            else:
                print('3.2 - Calculating Pawn Moves')
                moves = self.__get_pawn_moves(
                    board,
                    piece,
                )
            print(moves)
            if len(moves) > 0:
                all_moves.append((piece, moves))
        if len(all_moves) > 0:
            return self.__move_result(all_moves)
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
