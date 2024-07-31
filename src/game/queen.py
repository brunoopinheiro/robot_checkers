from game.piece import Piece
from proto.messages import (
    Piece as ProtoPiece,
    PieceType,
)


class Queen(Piece):

    @property
    def move_length(self) -> int:
        return 7

    @property
    def jump_length(self) -> int:
        return 7

    def to_proto(self) -> ProtoPiece:
        return ProtoPiece(
            self.coordinates.to_proto(),
            self.color,
            PieceType.QUEEN,
        )
