from checkers_mapping_kanova import dicionario_kAnova
from checkers_mapping_Kinova import dicionario_kinova


# def mapping_bounding_boxes(dict_yolo, mapped):
#     key, coordinates_yolo = dict_yolo.items()
#     for coordinates in mapped.values():
#         if all([([(coordinate_yolo[k] > coordinates[k]*0.8) or (coordinate_yolo[k] < coordinates[k]*1.2)] for coordinate_yolo in coordinates_yolo)] for k in range(4)):          
#             return coordinates_yolo[key]
        

mapeadas_kAnova = {'a1': [450, 140, 400, 90], 'a3': [448, 240, 398, 190], 'a5': [446, 290, 396, 240], 'a7': [444, 390, 394, 340], 
 'b2': [400, 191, 350, 141], 'b4': [398, 291, 348, 241], 'b6': [396, 391, 346, 341], 'b8': [394, 491, 344, 441], 
 'c1': [350, 142, 300, 92], 'c3': [348, 242, 298, 192], 'c5': [346, 292, 296, 242], 'c7': [344, 392, 294, 342], 
 'd2': [300, 193, 250, 143], 'd4': [298, 293, 248, 243], 'd6': [296, 393, 246, 343], 'd8': [294, 493, 244, 443], 
 'e1': [250, 144, 200, 94], 'e3': [248, 244, 198, 194], 'e5': [246, 344, 196, 294], 'e7': [244, 444, 144, 394], 
 'f2': [200, 195, 150, 145], 'f4': [198, 295, 148, 245], 'f6': [196, 395, 146, 345], 'f8': [194, 495, 144, 445], 
 'g1': [150, 146, 100, 96], 'g3': [148, 246, 98, 196], 'g5': [146, 346, 96, 296], 'g7': [144, 446, 94, 396], 
 'h2': [100, 197, 50, 147], 'h4': [98, 297, 48, 247], 'h6': [96, 397, 46, 347], 'h8': [94, 497, 44, 447]}




dicio = [{'name': 'green', 'class': 0, 'confidence': 0.94991, 'box': {'x1': 200.03036, 'y1': 390.61334, 'x2': 234.55609, 'y2': 428.38318}}, 
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

# print(mapping_bounding_boxes(dicio, mapeadas))
