from game.coordinates import Coordinates
from proto.messages import PieceType
from neural_network.detection_classes import DetectionClasses


from dataclasses import dataclass


@dataclass
class DetectionPiece:

    piece_class: DetectionClasses
    coords: Coordinates
    color: str
    piece_type: PieceType
