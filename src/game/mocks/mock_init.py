from neural_network.coords_parser import (
    DetectionPiece,
    DetectionClasses,
    Coordinates,
    PieceType,
)

INITIAL_GAME = [
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='a', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='a', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='b', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='d', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='f', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='h', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='a', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='c', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='d', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='d', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='e', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='g', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
]

FIRST_MOVE = [
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='a', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='b', row=4),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='b', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='d', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='f', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='h', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='a', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='c', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='d', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='d', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='e', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='g', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
]

THIRD_MOVE = [
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='a', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='d', row=6),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='b', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='c', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='d', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='e', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='f', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=1),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='g', row=3),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN,
        coords=Coordinates(col='h', row=2),
        color='green',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='a', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='b', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='c', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    # DetectionPiece(
    #     piece_class=DetectionClasses.PURPLE,
    #     coords=Coordinates(col='c', row=5),
    #     color='purple',
    #     piece_type=PieceType.PAWN,
    # ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='d', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='e', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='f', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='g', row=7),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=6),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE,
        coords=Coordinates(col='h', row=8),
        color='purple',
        piece_type=PieceType.PAWN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.GREEN_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='green',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
    DetectionPiece(
        piece_class=DetectionClasses.PURPLE_CHECKER,
        coords=Coordinates(col='z', row=9),
        color='purple',
        piece_type=PieceType.QUEEN,
    ),
]
