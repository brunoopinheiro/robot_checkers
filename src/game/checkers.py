from __future__ import annotations
from board import Board
from piece import Coordinates, Piece
from pawn import Pawn


class Checkers:
    # "⬛" for filled spaced
    # "⬜" for blank space
    # "🟣" for Purple pieces
    # "🟢" for Green pieces

    __instance = None

    @property
    def p1_pieces(self) -> list[Piece]:
        return self.__p1_pieces

    @property
    def p2_pieces(self) -> list[Piece]:
        return self.__p2_pieces

    def __new__(cls, *args, **kwargs) -> Checkers:
        if Checkers.__instance is None:
            Checkers.__instance = super(Checkers, cls).__new__(cls)
        return Checkers.__instance

    def __init__(
        self,
    ) -> None:
        self.__board = Board()
        self.__p1_pieces: list[Piece] = []
        self.__p2_pieces: list[Piece] = []

    def __initial_pieces(self) -> None:
        cols = Board.columns
        for i, c in enumerate(cols):
            if i % 2 == 0:
                # 2 verde (1, 3), 1 roxa (7)
                pg1 = Pawn(
                    coordinates=Coordinates(c, 1),
                    color='green',
                    icon='🟢',
                )
                pg2 = Pawn(
                    coordinates=Coordinates(c, 3),
                    color='green',
                    icon='🟢',
                )
                self.__p1_pieces.append(pg1)
                self.__p1_pieces.append(pg2)
                pp1 = Pawn(
                    coordinates=Coordinates(c, 7),
                    color='purple',
                    icon='🟣',
                )
                self.__p2_pieces.append(pp1)
            else:
                # 1 verde (2), 2 roxa (6, 8)
                pg1 = Pawn(
                    coordinates=Coordinates(c, 2),
                    color='green',
                    icon='🟢',
                )
                self.__p1_pieces.append(pg1)
                pp1 = Pawn(
                    coordinates=Coordinates(c, 6),
                    color='purple',
                    icon='🟣',
                )
                pp2 = Pawn(
                    coordinates=Coordinates(c, 8),
                    color='purple',
                    icon='🟣',
                )
                self.__p2_pieces.append(pp1)
                self.__p2_pieces.append(pp2)

    def _place_piece(
            self,
            piece: Piece,
            old_coords: Coordinates,
    ) -> None:
        self.__board.place_piece(piece, piece.coordinates, old_coords)

    def start_game(self) -> None:
        self.__initial_pieces()
        for piece1, piece2 in zip(self.__p1_pieces, self.__p2_pieces):
            self._place_piece(piece1, piece1.coordinates)
            self._place_piece(piece2, piece2.coordinates)

    def board_state(self) -> None:
        self.__board.board_state()
