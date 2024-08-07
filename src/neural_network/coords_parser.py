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
        #       x1   y1   x2   y2
        'a1': [470, 420, 530, 470],
        'a3': [470, 320, 530, 370],
        'a5': [470, 220, 530, 270],
        'a7': [470, 120, 530, 170],
        # -------------------------
        'b2': [430, 370, 480, 420],
        'b4': [430, 270, 480, 320],
        'b6': [430, 170, 480, 220],
        'b8': [430, 70, 480, 120],
        # -------------------------
        'c1': [370, 420, 430, 470],
        'c3': [370, 320, 430, 370],
        'c5': [370, 220, 430, 270],
        'c7': [370, 120, 430, 170],
        # -------------------------
        'd2': [330, 370, 380, 420],
        'd4': [330, 270, 380, 320],
        'd6': [330, 170, 380, 220],
        'd8': [330, 70, 380, 120],
        # -------------------------
        'e1': [280, 420, 330, 470],
        'e3': [280, 320, 330, 370],
        'e5': [280, 220, 330, 270],
        'e7': [280, 120, 330, 170],
        # -------------------------
        'f2': [230, 380, 280, 420],
        'f4': [230, 280, 280, 320],
        'f6': [230, 180, 280, 220],
        'f8': [230, 80, 280, 120],
        # -------------------------
        'g1': [170, 430, 220, 480],
        'g3': [170, 330, 220, 380],
        'g5': [170, 230, 220, 280],
        'g7': [170, 130, 220, 180],
        # -------------------------
        'h2': [130, 380, 180, 420],
        'h4': [130, 280, 180, 320],
        'h6': [130, 180, 180, 220],
        'h8': [130, 80, 180, 120],
    }

    _kanova_dict = {
        'a1': [440, 380, 490, 430],
        'a3': [340, 380, 390, 430],
        'a5': [240, 380, 290, 430],
        'a7': [140, 380, 190, 430],
        'b2': [390, 330, 440, 380],
        'b4': [290, 330, 340, 380],
        'b6': [190, 330, 240, 380],
        'b8': [90, 330, 140, 380],
        'c1': [440, 280, 490, 330],
        'c3': [340, 280, 390, 330],
        'c5': [240, 280, 290, 330],
        'c7': [140, 280, 190, 330],
        'd2': [390, 230, 440, 280],
        'd4': [290, 230, 340, 280],
        'd6': [190, 230, 240, 280],
        'd8': [90, 230, 140, 280],
        'e1': [440, 180, 490, 230],
        'e3': [340, 180, 390, 230],
        'e5': [240, 180, 290, 230],
        'e7': [140, 180, 190, 230],
        'f2': [390, 130, 440, 180],
        'f4': [290, 130, 340, 180],
        'f6': [190, 130, 240, 180],
        'f8': [90, 130, 140, 180],
        'g1': [440, 80, 490, 130],
        'g3': [340, 80, 390, 130],
        'g5': [240, 80, 290, 130],
        'g7': [140, 80, 190, 130],
        'h2': [390, 30, 440, 80],
        'h4': [290, 30, 340, 80],
        'h6': [190, 30, 240, 80],
        'h8': [90, 30, 140, 80],
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
        tolerance: int = 15,
    ) -> List[DetectionPiece]:
        map_dict = CoordsParser.__get_dict(refference_dict)
        locations = []
        confiable_detections = CoordsParser.__filter_conf(input_list)
        for piece in confiable_detections:
            box_piece = piece['box']
            box_x1 = box_piece['x1']
            box_y1 = box_piece['y1']
            box_x2 = box_piece['x2']
            box_y2 = box_piece['y2']
            box_x = (box_x1 + box_x2) / 2
            box_y = (box_y1 + box_y2) / 2
            print(f'Box: {box_piece}')
            found = False
            piece_class, piece_type, color = CoordsParser.__get_class(
                int(piece['class'])
            )
            for square, coords in map_dict.items():
                x1, y1, x2, y2 = coords
                conditions = (
                    ((x1 < (box_x-tolerance) < x2)
                        or (x1 < (box_x+tolerance) < x2))
                    and ((y1 < (box_y-tolerance) < y2)
                         or (y1 < (box_y+tolerance) < y2))
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
                print(f'Increasing tollerance to {new_t}')
                return CoordsParser.map_pieces(
                    confiable_detections,
                    refference_dict,
                    new_t,
                )
        for loc in locations:
            print(loc)
        return locations
