from piece import Piece


class Queen(Piece):

    @property
    def move_length(self) -> int:
        return 7

    @property
    def jump_length(self) -> int:
        return 7
