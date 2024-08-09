from neural_network.detection_piece import DetectionPiece
from neural_network.detection_classes import DetectionClasses
from game.coordinates import Coordinates
from proto.messages import PieceType
from neural_network.game_ai import GameAI
from neural_network.rectfier.rectifier import Rectifier
from typing import List, Tuple


class CoordsParser:

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
    def detect_checkboard(image_source, show=False):
        # Rectify image
        rectified_img = Rectifier.rectify(image_source, show)
        # create a dictionary with the coordinates of each square
        reff_map = Rectifier.map_board(rectified_img)
        return rectified_img, reff_map

    @staticmethod
    def map_pieces(
        input_list,
        refference_dict,
    ) -> List[DetectionPiece]:
        locations = []
        for piece in input_list:
            box_piece = piece['box']
            box_x1 = box_piece['x1']
            box_y1 = box_piece['y1']
            box_x2 = box_piece['x2']
            box_y2 = box_piece['y2']
            center_x = (box_x1 + box_x2) / 2
            center_y = (box_y1 + box_y2) / 2
            print(f'Box: {box_piece}')
            piece_class, piece_type, color = CoordsParser.__get_class(
                int(piece['class'])
            )
            found = False
            for square, coords in refference_dict.items():
                # this should change
                _, _, x2, y2, x3, y3, _, _ = coords
                condition = (
                    (center_x > x3 and center_x < x2)
                    and (center_y > y2 and center_y < y3)
                )
                if found is False and condition is True:
                    found = True
                    sqr_name = GameAI.board_as_int.get(square)[0]
                    d_piece = DetectionPiece(
                        piece_class,
                        coords=Coordinates(sqr_name[0], int(sqr_name[1])),
                        color=color,
                        piece_type=piece_type,
                    )
                    locations.append(d_piece)
        return locations
