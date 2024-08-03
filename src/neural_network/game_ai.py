from typing import List
from game.checkers import Checkers
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
