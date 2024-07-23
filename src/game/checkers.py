from __future__ import annotations
from board import Board
from piece import Coordinates, Piece
from pawn import Pawn
from queen import Queen
from enum import Enum


OUT_OF_BOUNDS = "You've tried to go out of the board."


class MovementTypes(Enum):

    MOVE = 1
    JUMP = 2


class Checkers:
    # "⬛" for filled spaced
    # "⬜" for blank space
    # "🟣" for Purple pieces
    # "🟢" for Green pieces

    __instance = None
    __colmap: dict[str, int] = {val: idx
                                for idx, val in enumerate(Board.columns)}

    def __new__(cls, *args, **kwargs) -> Checkers:
        if Checkers.__instance is None:
            Checkers.__instance = super(Checkers, cls).__new__(cls)
        return Checkers.__instance

    def __init__(
        self,
    ) -> None:
        self.__board = Board()
        self.p1_pieces: list[Piece] = []
        self.p2_pieces: list[Piece] = []

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
                self.p1_pieces.append(pg1)
                self.p1_pieces.append(pg2)
                pp1 = Pawn(
                    coordinates=Coordinates(c, 7),
                    color='purple',
                    icon='🟣',
                )
                self.p2_pieces.append(pp1)
            else:
                # 1 verde (2), 2 roxa (6, 8)
                pg1 = Pawn(
                    coordinates=Coordinates(c, 2),
                    color='green',
                    icon='🟢',
                )
                self.p1_pieces.append(pg1)
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
                self.p2_pieces.append(pp1)
                self.p2_pieces.append(pp2)

    def __distance(self, origin: Coordinates, destiny: Coordinates) -> int:
        o_col, o_row = origin
        d_col, d_row = destiny
        a: tuple[int, int] = (Checkers.__colmap[o_col], o_row)
        b: tuple[int, int] = (Checkers.__colmap[d_col], d_row)
        print(a, b)
        c = (abs(a[0] - b[0]), abs(a[1] - b[1]))
        return max(c)

    def _place_piece(
            self,
            piece: Piece,
            old_coords: Coordinates,
    ) -> None:
        self.__board.place_piece(piece, piece.coordinates, old_coords)

    def _check_valid_move(
            self,
            piece: Piece,
            destiny: Coordinates,
    ) -> bool:
        try:
            if self.__distance(piece.coordinates, destiny) > piece.move_length:
                return False
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def _check_valid_jump(
            self,
            piece: Piece,
            destiny: Coordinates,
    ) -> bool:
        try:
            if self.__distance(piece.coordinates, destiny) > piece.jump_length:
                print('Your jump is too long')
                return False
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def start_game(self) -> None:
        self.__initial_pieces()
        for piece1, piece2 in zip(self.p1_pieces, self.p2_pieces):
            self._place_piece(piece1, piece1.coordinates)
            self._place_piece(piece2, piece2.coordinates)

    def board_state(self) -> None:
        self.__board.board_state()

    def get_piece_by_coord(self, coord: Coordinates) -> Piece | None:
        for piece in self.p1_pieces:
            if piece.coordinates == coord:
                return piece
        for piece in self.p2_pieces:
            if piece.coordinates == coord:
                return piece
        return None

    def __remove_piece(self, piece_coordinates: Coordinates) -> bool:
        self.__board.remove_piece(piece_coordinates)
        for idx, piece in enumerate(self.p1_pieces):
            if piece.coordinates == piece_coordinates:
                self.p1_pieces.pop(idx)
        for idx, piece in enumerate(self.p2_pieces):
            if piece.coordinates == piece_coordinates:
                self.p2_pieces.pop(idx)

    def __swap_piece(self, new_piece: Piece) -> None:
        for idx, piece in enumerate(self.p1_pieces):
            if piece.coordinates == new_piece.coordinates:
                self.p1_pieces[idx] = new_piece
        for idx, piece in enumerate(self.p2_pieces):
            if piece.coordinates == new_piece.coordinates:
                self.p2_pieces[idx] = new_piece

    def move_piece(self, origin: Coordinates, destiny: Coordinates) -> bool:
        try:
            if self.__board.is_empty(origin):
                return False
            if not self.__board.is_empty(destiny):
                return False
            piece = self.get_piece_by_coord(origin)
            if self._check_valid_move(piece, destiny) is False:
                return False
            piece.move(destiny)
            self._place_piece(piece, origin)
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def jump_piece(
            self,
            origin: Coordinates,
            destiny: Coordinates,
            target_piece: Coordinates,
    ) -> bool:
        if self.__board.is_empty(origin):
            return False
        if not self.__board.is_empty(destiny):
            return False
        piece = self.get_piece_by_coord(origin)
        middle_piece = self.get_piece_by_coord(target_piece)
        if middle_piece is None:
            return False
        if piece.color == middle_piece.color:
            return False
        if self._check_valid_jump(piece, destiny) is False:
            return False
        piece.move(destiny)
        self._place_piece(piece, origin)
        self.__remove_piece(middle_piece.coordinates)
        return True

    def _promote_piece(
            self,
            coordinates: Coordinates,
    ) -> Queen:
        piece = self.get_piece_by_coord(coordinates)
        queen = None
        if piece.color == 'green':
            queen = Queen(
                coordinates=piece.coordinates,
                color=piece.color,
                icon='❇️',
            )
        if piece.color == 'purple':
            queen = Queen(
                coordinates=piece.coordinates,
                color=piece.color,
                icon='⚛️'
            )
        self.__remove_piece(piece.coordinates)
        self._place_piece(queen, queen.coordinates)
        self.__swap_piece(queen)
