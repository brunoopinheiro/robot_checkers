from typing import List, Tuple
from game.board import Board, Coordinates
from game.piece import Piece
from neural_network.coords_parser import DetectionPiece
from dataclasses import dataclass
from enum import Enum, auto


class GameAIResultType(Enum):

    MOVE = auto()
    JUMP = auto()


@dataclass
class GameAIResult:

    # tipo jogada (move, jump)
    result_type: GameAIResultType
    # origin
    origin: Coordinates
    # destiny
    destiny: Coordinates
    # target (nullable)
    target: List[Tuple[Coordinates, Coordinates]]


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

    @staticmethod
    def __detect_move(
        board: Board,
        pieces_list: List[DetectionPiece],
    ):
        moved = None
        i = 0
        while moved is None and i < len(pieces_list):
            d_piece = pieces_list[i]
            if board.is_empty(d_piece.coords):
                moved = d_piece
            i += 1
        # from adjacent squares, what is not there anymore
        key = f'{moved.coords.col}{moved.coords.row}'
        adjs = GameAI.adjascent_squares.get(key)
        for coord in adjs:
            cd = Coordinates(coord[0], int(coord[1]))
            if not board.is_empty(cd):
                return GameAIResult(
                    result_type=GameAIResultType.MOVE,
                    origin=cd,
                    destiny=d_piece.coords,
                    target=[],
                )

    @staticmethod
    def __find_jumper(
        board: Board,
        pieces_list: List[DetectionPiece],
        color: str,
    ) -> Coordinates:
        """This Represents the coordinates
        of the piece after all the jumps."""
        moved = None
        i = 0
        while moved is None and i < len(pieces_list):
            d_piece = pieces_list[i]
            if d_piece.color == color and board.is_empty(d_piece.coords):
                moved = d_piece
            i += 1
        return d_piece.coords

    @staticmethod
    def __detect_jump(
        jumps: int,
        p1_pieces: List[Piece],
        p2_pieces: List[Piece],
        board: Board,
        pieces_list: List[DetectionPiece],
    ):
        p1color = p1_pieces[0].color
        p2color = p2_pieces[0].color
        countp1 = 0
        for d_piece in pieces_list:
            if d_piece.color == p1color:
                countp1 += 1
        destiny = None
        if countp1 < len(p1_pieces):
            # this means p2 executed the jumps
            # find the piece who moved
            destiny = GameAI.__find_jumper(
                board,
                pieces_list,
                p2color,
            )
        else:
            # p1 executed the jumps
            # find the piece who moved
            destiny = GameAI.__find_jumper(
                board,
                pieces_list,
                p1color,
            )
        # it had an adjascent adversary with an empty square next to it
        # repeat by the number o jumps
        list_jumps = [None] * jumps
        origin = None
        i = 0
        while i < jumps:
            i += 1
            key = f'{destiny.col}{destiny.row}'
            adjs = GameAI.adjascent_squares.get(key)
            for coord in adjs:
                cd = Coordinates(coord[0], int(coord[1]))
                if not board.is_empty(cd):
                    # check if coord adj is empty
                    target = cd
                    tkey = f'{target.col}{target.row}'
                    tadjs = GameAI.adjascent_squares.get(tkey)
                    for tcoord in tadjs:
                        tcd = Coordinates(tcoord[0], int(tcoord[1]))
                        if i == jumps:
                            if not board.is_empty(tcd):
                                origin = tcd
                                list_jumps[i-1] = (target, destiny)
                                destiny = origin
                        else:
                            if board.is_empty(tcd):  # missing one validation
                                origin = tcd
                                list_jumps[i-1] = (target, destiny)
                                destiny = origin
        return GameAIResult(
            result_type=GameAIResultType.JUMP,
            origin=origin,
            destiny=destiny,
            target=list_jumps,
        )

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
    def detect_play(
        board: Board,
        p1_pieces: List[Piece],
        p2_pieces: List[Piece],
        pieces_list: List[DetectionPiece],
    ) -> GameAIResult:
        filtered_pieces = GameAI.filter_outerboard(pieces_list)
        new_count = len(filtered_pieces)
        old_count = (len(p1_pieces) + len(p2_pieces))
        if new_count == old_count:
            return GameAI.__detect_move(
                board,
                filtered_pieces,
            )
        if new_count < old_count:
            jumps = old_count - new_count
            return GameAI.__detect_jump(
                jumps,
                p1_pieces,
                p2_pieces,
                board,
                filtered_pieces,
            )
