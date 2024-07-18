from dataclasses import dataclass
from piece import Piece, Coordinates


@dataclass
class Square:

    col: str
    row: int
    movable: bool
    content: Piece


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
