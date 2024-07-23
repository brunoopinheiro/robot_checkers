from piece import Piece


class Pawn(Piece):

    @property
    def move_length(self) -> int:
        return 1

    @property
    def jump_length(self) -> int:
        return 2
