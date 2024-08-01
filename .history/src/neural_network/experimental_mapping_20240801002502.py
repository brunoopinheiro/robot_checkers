from checkers_mapping_kanova import dicionario_kAnova
from checkers_mapping_kinova import dicionario_kinova



def mapping_bounding_box(dict_yolo, dict_checkers, tolerance=30):
    locations = []
    for piece in dict_yolo:
        box_piece = piece['box']
        found = False
        for square, coords in dict_checkers.items():
            (x1_square, y1_square, x2_square, y2_square) = coords
            if (
                (x1_square + tolerance < box_piece['x1'] or x1_square - tolerance < box_piece['x1']) and
                (y1_square + tolerance < box_piece['y1'] or y1_square - tolerance > box_piece['y1']) and
                (x2_square + tolerance > box_piece['x2']) and
                (y2_square + tolerance > box_piece['y2'])
            ):
                locations.append((piece, square))
                found = True
                break
        if not found:
            locations.append((piece, None))
    return locations


def robot_board():
        robot_board = input("kAnova (2) or kinova (1)?: 'q' to exit: ")
        while robot_board not in ['1', '2'] and robot_board != 'q':
                robot_board = input("kAnova (2) or kinova (1)?: 'q' to exit: ")
        
        if robot_board == '1':
                dict_robot_board = dicionario_kinova
        elif robot_board == '2':
                dict_robot_board = dicionario_kAnova
        else:
                return 'None of the robots were selected'
        return dict_robot_board

        


[{'name': 'green', 'class': 0, 'confidence': 0.92639, 'box': {'x1': 82.19824, 'y1': 242.47702, 'x2': 124.43007, 'y2': 277.96402}}, {'name': 'green', 'class': 0, 'confidence': 0.89701, 'box': {'x1': 391.77356, 'y1': 245.06636, 'x2': 427.38983, 'y2': 279.52399}}, {'name': 'green', 'class': 0, 'confidence': 0.88918, 'box': {'x1': 190.78366, 'y1': 145.63388, 'x2': 227.77084, 'y2': 181.99374}}, {'name': 'green', 'class': 0, 'confidence': 0.87085, 'box': {'x1': 340.96881, 'y1': 194.4679, 'x2': 375.68768, 'y2': 229.8226}}, {'name': 'green', 'class': 0, 'confidence': 0.84605, 'box': {'x1': 142.10675, 'y1': 191.16925, 'x2': 179.45728, 'y2': 225.12469}}, {'name': 'purple', 'class': 2, 'confidence': 0.82844, 'box': {'x1': 191.53006, 'y1': 35.45227, 'x2': 228.0199x1': 293.01724, 'y1': 138.0175, 'x2': 326.03653, 'y2': 174.01268}}, {'name': 'purple', 'class': 2, 'confidence': 0.65843, 'box': {'x1': 300.3092, 'y1': 34.3768, 'x2': 333.14441, 'y2': 77.12195}}]
res = mapping_bounding_box(dict_yolo_example, robot_board())
for piece, square in res:
    print(f"The piece {piece['name']} is placed in the square {square}")
