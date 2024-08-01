from enum import Enum
from neural_network.detection_classes import DetectionClasses
from game.coordinates import Coordinates
from proto.messages import PieceType
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class DetectionPiece:

    piece_class: DetectionClasses
    coords: Coordinates
    color: str
    piece_type: PieceType


class RefferenceDict(Enum):

    KINOVA = 1
    KANOVA = 2


class CoordsParser:

    _kinova_dict = {
        'a1': [100, 50, 150, 100],
        'a3': [200, 50, 250, 100],
        'a5': [300, 50, 350, 100],
        'a7': [400, 50, 450, 100],
        'b2': [150, 100, 200, 150],
        'b4': [250, 100, 300, 150],
        'b6': [350, 100, 400, 150],
        'b8': [450, 100, 500, 150],
        'c1': [100, 150, 150, 200],
        'c3': [200, 150, 250, 200],
        'c5': [300, 150, 350, 200],
        'c7': [400, 150, 450, 200],
        'd2': [150, 200, 200, 250],
        'd4': [250, 200, 300, 250],
        'd6': [350, 200, 400, 250],
        'd8': [450, 200, 500, 250],
        'e1': [100, 250, 150, 300],
        'e3': [200, 250, 250, 300],
        'e5': [300, 250, 350, 300],
        'e7': [400, 250, 450, 300],
        'f2': [150, 300, 200, 350],
        'f4': [250, 300, 300, 350],
        'f6': [350, 300, 400, 350],
        'f8': [450, 300, 500, 350],
        'g1': [100, 350, 150, 400],
        'g3': [200, 350, 250, 400],
        'g5': [300, 350, 350, 400],
        'g7': [400, 350, 450, 400],
        'h2': [150, 400, 200, 450],
        'h4': [250, 400, 300, 450],
        'h6': [350, 400, 400, 450],
        'h8': [450, 400, 500, 450],
    }

    _kanova_dict = {
        'a1': [90, 30, 140, 80],
        'a3': [190, 30, 240, 80],
        'a5': [290, 30, 340, 80],
        'a7': [390, 30, 440, 80],
        'b2': [140, 80, 190, 130],
        'b4': [240, 80, 290, 130],
        'b6': [340, 80, 390, 130],
        'b8': [440, 80, 490, 130],
        'c1': [90, 130, 140, 180],
        'c3': [190, 130, 240, 180],
        'c5': [290, 130, 340, 180],
        'c7': [390, 130, 440, 180],
        'd2': [140, 180, 190, 230],
        'd4': [240, 180, 290, 230],
        'd6': [340, 180, 390, 230],
        'd8': [440, 180, 490, 230],
        'e1': [90, 230, 140, 280],
        'e3': [190, 230, 240, 280],
        'e5': [290, 230, 340, 280],
        'e7': [390, 230, 440, 280],
        'f2': [140, 280, 190, 330],
        'f4': [240, 280, 290, 330],
        'f6': [340, 280, 390, 330],
        'f8': [440, 280, 490, 330],
        'g1': [90, 330, 140, 380],
        'g3': [190, 330, 240, 380],
        'g5': [290, 330, 340, 380],
        'g7': [390, 330, 440, 380],
        'h2': [140, 380, 190, 430],
        'h4': [240, 380, 290, 430],
        'h6': [340, 380, 390, 430],
        'h8': [440, 380, 490, 430],
    }

    @staticmethod
    def __get_dict(ref_dict: RefferenceDict):
        if ref_dict == RefferenceDict.KINOVA:
            return CoordsParser._kinova_dict
        else:
            return CoordsParser._kanova_dict

    @staticmethod
    def __get_class(class_num: int) -> Tuple[DetectionClasses, PieceType, str]:
        green = 'green'
        purple = 'purple'
        if class_num == DetectionClasses.GREEN.value:
            return (
                DetectionClasses.GREEN,
                PieceType.PAWN,
                green,
            )
        elif class_num == DetectionClasses.GREEN_CHECKER.value:
            return (
                DetectionClasses.GREEN_CHECKER,
                PieceType.QUEEN,
                green,
            )
        elif class_num == DetectionClasses.PURPLE.value:
            return (
                DetectionClasses.PURPLE,
                PieceType.PAWN,
                purple,
            )
        elif class_num == DetectionClasses.PURPLE_CHECKER.value:
            return (
                DetectionClasses.PURPLE,
                PieceType.QUEEN,
                purple,
            )
        else:
            raise SystemError('Detection Class Not Found')

    @staticmethod
    def __filter_conf(input_list):
        return list(filter(lambda x: x['confidence'], input_list))

    @staticmethod
    def map_pieces(
        input_list,
        refference_dict: RefferenceDict,
        tolerance: int = 25,
    ) -> List[DetectionPiece]:
        map_dict = CoordsParser.__get_dict(refference_dict)
        locations = []
        print(input_list)
        print(f'Old Input: {len(input_list)}')
        confiable_detections = CoordsParser.__filter_conf(input_list)
        print(confiable_detections)
        print(f'Filtered: {len(confiable_detections)}')
        for piece in confiable_detections:
            box_piece = piece['box']
            box_x1 = box_piece['x1']
            box_y1 = box_piece['y1']
            box_x2 = box_piece['x2']
            box_y2 = box_piece['y2']
            found = False
            piece_class, piece_type, color = CoordsParser.__get_class(
                int(piece['class'])
            )
            for square, coords in map_dict.items():
                x1, y1, x2, y2 = coords
                conditions = (
                    (x1 + tolerance < box_x1 or x1 - tolerance < box_x1) and
                    (y1 + tolerance < box_y1 or y1 - tolerance < box_y1) and
                    (x2 + tolerance > box_x2) and
                    (y2 + tolerance > box_y2)
                )
                if not found and conditions is True:
                    d_piece = DetectionPiece(
                        piece_class,
                        Coordinates(square[0], int(square[1])),
                        color,
                        piece_type,
                    )
                    locations.append(d_piece)
                    found = True
            if not found and piece_type == PieceType.QUEEN:
                # if a piece coordinate was not found,
                # assume it is outside the board
                d_piece = DetectionPiece(
                    piece_class,
                    Coordinates('z', 9),
                    color,
                    piece_type,
                )
                locations.append(d_piece)
            elif not found and piece_type != PieceType.PAWN:
                new_t = tolerance + 5
                return CoordsParser.map_pieces(
                    confiable_detections,
                    refference_dict,
                    new_t,
                )
        return locations
