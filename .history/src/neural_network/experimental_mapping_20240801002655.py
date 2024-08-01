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

        

#runs/detect/predict2
dict_yolo_example = 
res = mapping_bounding_box(dict_yolo_example, robot_board())
for piece, square in res:
    print(f"The piece {piece['name']} is placed in the square {square}")
