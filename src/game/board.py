from dataclasses import dataclass
from piece import Piece


@dataclass
class Square:

    col: str
    row: int
    movable: bool
    content: Piece


class Board:

    filled = 'xxx'
    empty = '   '
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    rows = (1, 2, 3, 4, 5, 6, 7, 8)

    def board_state(self) -> str:
        for idx, row in enumerate(self.__board):
            r = [Board.filled if sqr.movable else Board.empty for sqr in row]
            letter = Board.columns[idx].upper()
            base = ' |{}|{}|{}|{}|{}|{}|{}|{}|'.format(*r)
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
            row = []
            for idc, col in enumerate(Board.columns):
                access_dict[f'{row}{col}'] = f'{idc}{idr}'
                sqr = Square(col, row, movable, None)
                row.append(sqr)
                movable = False if movable is True else True
            board.append(row)
            movable = False if movable is True else True
        self.__access = access_dict
        self.__board: list[list[Square]] = board

    def get_square(self, col: str, row: int):
        key = f'{row}{col}'.lower()
        value = self.__access[key]
        return value
