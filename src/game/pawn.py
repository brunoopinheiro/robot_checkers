from game.coordinates import Coordinates
from game.piece import Piece
from proto.messages import (
    Piece as ProtoPiece,
    PieceType,
)


class Pawn(Piece):

    def __init__(
            self,
            coordinates: Coordinates,
            color: str,
            icon: str,
            promote_row: int,
    ) -> None:
        super().__init__(coordinates, color, icon)
        self.__promote = promote_row

    @property
    def promote_row(self) -> int:
        return self.__promote

    @property
    def move_length(self) -> int:
        return 1

    @property
    def jump_length(self) -> int:
        return 2

    def to_proto(self) -> ProtoPiece:
        return ProtoPiece(
            self.coordinates.to_proto(),
            self.color,
            PieceType.PAWN,
        )
