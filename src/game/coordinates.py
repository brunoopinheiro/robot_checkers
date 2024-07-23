from __future__ import annotations
from dataclasses import dataclass


COLUMNS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
ROWS = (1, 2, 3, 4, 5, 6, 7, 8)


@dataclass
class Coordinates:

    col: str
    row: int

    def update(self, col_move: int, row_move: int) -> None:
        idx = COLUMNS.index(self.col)
        if col_move > 0:
            for _ in range(col_move):
                idx += 1
        else:
            for _ in range(col_move):
                idx -= 1
        self.col = COLUMNS[idx]
        self.row += row_move

    def __iter__(self):
        return iter((self.col, self.row))

    def __eq__(self, other: Coordinates) -> bool:
        if self.col == other.col and self.row == other.row:
            return True
        return False
