from checkers_mapping_kanova import dicionario_kAnova
from checkers_mapping_kinova import dicionario_kinova



def mapping_bounding_box(dict_yolo, dict_checkers, tolerance=20):
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

        


dict_yolo_example = [{'name': 'green', 'class': 0, 'confidence': 0.94991, 'box': {'x1': 200.03036, 'y1': 390.61334, 'x2': 234.55609, 'y2': 428.38318}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.94464, 'box': {'x1': 256.89453, 'y1': 141.41737, 'x2': 288.0083, 'y2': 183.94804}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.83168, 'box': {'x1': 251.14105, 'y1': 341.15958, 'x2': 285.56879, 'y2': 376.21658}},
        {'name': 'green', 'class': 0, 'confidence': 0.82021, 'box': {'x1': 307.83765, 'y1': 291.51468, 'x2': 341.66614, 'y2': 324.92612}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.81889, 'box': {'x1': 145.79803, 'y1': 438.32843, 'x2': 180.28506, 'y2': 479.47736}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.81593, 'box': {'x1': 299.20618, 'y1': 189.36957, 'x2': 332.96277, 'y2': 227.05292}}, 
        {'name': 'purple', 'class': 2, 'confidence': 0.8098, 'box': {'x1': 405.26947, 'y1': 191.60245, 'x2': 443.80292, 'y2': 228.71255}}, 
        {'name': 'purple', 'class': 2, 'confidence': 0.79538, 'box': {'x1': 405.40329, 'y1': 298.3782, 'x2': 445.17209, 'y2': 333.52353}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.78915, 'box': {'x1': 342.74579, 'y1': 251.41248, 'x2': 382.6225, 'y2': 287.34418}}, 
        {'name': 'purple', 'class': 2, 'confidence': 0.77226, 'box': {'x1': 404.80508, 'y1': 401.68747, 'x2': 444.47598, 'y2': 439.84323}}, 
        {'name': 'green', 'class': 0, 'confidence': 0.76707, 'box': {'x1': 202.10918, 'y1': 80.49863, 'x2': 241.90288, 'y2': 126.32437}}, 
        {'name': 'purple', 'class': 2, 'confidence': 0.73438, 'box': {'x1': 412.07346, 'y1': 82.1969, 'x2': 450.21158, 'y2': 127.39244}}]


dict_yolo_example_2 = [{'name': 'green_checker', 'class': 1, 'confidence': 0.86634, 'box': {'x1': 408.70679, 'y1': 147.30063, 'x2': 446.5553, 'y2': 187.47476}}, {'name': 'green', 'class': 0, 'confidence': 0.56452, 'box': {'x1': 97.49442, 'y1': 158.63623, 'x2': 134.08328, 'y2': 194.53259}}, {'name': 'purple', 'class': 2, 'confidence': 0.5429, 'box': {'x1': 210.00185, 'y1': 158.84821, 'x2': 241.61784, 'y2': 195.59714}}, {'name': 'green_checker', 'class': 1, 'confidence': 0.51236, 'box': {'x1': 311.31769, 'y1': 156.26598, 'x2': 340.07855, 'y2': 193.68617}}]

res = mapping_bounding_box(dict_yolo_example_2, robot_board())
for piece, square in res:
    print(f"The [piece: {piece['name']}, class: {piece['class']}, confidence: {piece['confidence']}] is placed in the square {square}")
