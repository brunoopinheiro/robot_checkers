from dataclasses import dataclass
from typing import List
from game.piece import Piece, Coordinates
from game.queen import Queen
from proto.messages import (
    Square as ProtoSquare,
    Row,
    Board as ProtoBoard,
)


@dataclass
class Square:

    col: str
    row: int
    movable: bool
    content: Piece

    def to_proto(self) -> ProtoSquare:
        ctnt = None
        if self.content is not None:
            ctnt = self.content.to_proto()
        return ProtoSquare(
            self.col,
            self.row,
            self.movable,
            ctnt,
        )


class Board:

    filled = '⬛'
    empty = '⬜'
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    rows = (1, 2, 3, 4, 5, 6, 7, 8)

    def board_state(self) -> str:
        for idx, row_ in enumerate(self.__board):
            row = []
            for sqr in row_:
                if sqr.movable and sqr.content is not None:
                    row.append(sqr.content.icon)
                elif sqr.movable and sqr.content is None:
                    row.append(Board.filled)
                else:
                    row.append(Board.empty)
            letter = Board.columns[idx].upper()
            base = ' | {}| {}| {}| {}| {}| {}| {}| {}|'.format(*row)
            rowstr = letter + base
            print(rowstr)
            print('  +---+---+---+---+---+---+---+---+')
        br = Board.rows
        print('  | {} | {} | {} | {} | {} | {} | {} | {} |'.format(*br))

    def __init__(self) -> None:
        access_dict = {}
        board = []
        movable = True
        for idr, row in enumerate(Board.rows):
            row_list = []
            for idc, col in enumerate(Board.columns):
                access_dict[f'{row}{col}'] = f'{idc}{idr}'
                sqr = Square(col, row, movable, None)
                row_list.append(sqr)
                movable = False if movable is True else True
            board.append(row_list)
            movable = False if movable is True else True
        self.__access = access_dict
        self.__board: list[list[Square]] = board

    def to_proto(self):
        rows = [
            Row(squares=[sqr.to_proto() for sqr in board_row])
            for board_row in self.__board
        ]
        board = ProtoBoard(rows)
        return board

    def get_square(self, col: str, row: int):
        key = f'{row}{col}'.lower()
        value = self.__access[key]
        return int(value[0]), int(value[1])

    def place_piece(
            self,
            piece: Piece,
            newcoords: Coordinates,
            oldcoords: Coordinates,
    ) -> None:
        o_col, o_row = oldcoords
        n_col, n_row = newcoords
        board_col, board_row = self.get_square(o_col, o_row)
        newb_col, newb_row = self.get_square(n_col, n_row)
        self.__board[board_col][board_row].content = None
        self.__board[newb_col][newb_row].content = piece

    def remove_piece(
            self,
            coordinates: Coordinates,
    ) -> None:
        col, row = coordinates
        b_col, b_row = self.get_square(col, row)
        self.__board[b_col][b_row].content = None

    def is_empty(self, coords: Coordinates) -> bool:
        col, row = coords
        c, r = self.get_square(col, row)
        if self.__board[c][r].content is None:
            return True
        return False

    def __clear_board(self) -> None:
        for key in self.__access.keys():
            i, j = self.get_square(key[1], int(key[0]))
            self.__board[i][j].content = None

    def overwrite_board(self, pieces_list: List[Piece]):
        self.__clear_board()
        for piece in pieces_list:
            i, j = self.get_square(
                piece.coordinates.col,
                piece.coordinates.row,
            )
            self.__board[i][j].content = piece

    def _validate_capture(
            self,
            origin_coordinates: Coordinates,
            target_coordinates: Coordinates,
    ) -> int:
        """Returns the value of a possible capture.
        0 means it is not a valid capture.
        1 means it is a pawn capture.
        2 means it is a queen capture.

        Args:
            origin_coordinates (Coordinates):
                the coordinates of the jumping piece
            target_coordinates (Coordinates):
                the coordinates of the target piece

        Returns:
            int: The value of the capture
        """
        o_col, o_row = origin_coordinates
        t_col, t_row = target_coordinates
        o_c, o_r = self.get_square(o_col, o_row)
        t_c, t_r = self.get_square(t_col, t_row)
        origin = self.__board[o_c][o_r]
        target = self.__board[t_c][t_r]
        v_sum = 0
        if (origin.content is not None
                and target.content is not None
                and origin.content.color != target.content.color):
            v_sum += 1
            if isinstance(target.content, Queen):
                v_sum += 1
        return v_sum
