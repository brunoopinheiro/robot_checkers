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
        'a1': [480, 420, 530, 470],  
        'a3': [380, 420, 430, 470],
        'a5': [280, 420, 330, 470],
        'a7': [180, 420, 230, 470],
        'b2': [130, 370, 180, 420],
        'b4': [230, 370, 280, 420],
        'b6': [330, 370, 380, 420],
        'b8': [430, 370, 480, 420],
        'c1': [480, 320, 530, 370],
        'c3': [380, 320, 430, 370],
        'c5': [280, 320, 330, 370],
        'c7': [180, 320, 230, 370],
        'd2': [430, 270, 480, 320],
        'd4': [330, 270, 380, 320],
        'd6': [230, 270, 280, 320],
        'd8': [130, 270, 180, 320],
        'e1': [480, 220, 530, 270],
        'e3': [380, 220, 430, 270],
        'e5': [280, 220, 330, 270],
        'e7': [180, 220, 230, 270],
        'f2': [430, 170, 480, 220],
        'f4': [330, 170, 380, 220],
        'f6': [230, 170, 280, 220],
        'f8': [130, 170, 180, 220],
        'g1': [180, 120, 230, 170],
        'g3': [280, 120, 330, 170], 
        'g5': [380, 120, 430, 170],
        'g7': [480, 120, 530, 170],
        'h2': [430, 70, 480, 120],
        'h4': [330, 70, 380, 120],
        'h6': [230, 70, 280, 120],
        'h8': [130, 70, 180, 120],
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
