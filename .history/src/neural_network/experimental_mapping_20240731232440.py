from checkers_mapping_kanova import dicionario_kAnova
from checkers_mapping_Kinova import dicionario_kinova

def mapping_bounding_box(dict_yolo, dict_checkers_kanova, tolerancia=10):
    localizacoes = []

    for peca in dict_yolo:
        box_peca = peca['box']
        encontrou = False

        for casa, coords in dict_checkers_kanova.items():
            x1_casa, y1_casa, x2_casa, y2_casa = coords

            if (
                (x1_casa - tolerancia <= box_peca['x1'] <= x2_casa + tolerancia) and
                (y1_casa - tolerancia <= box_peca['y1'] <= y2_casa + tolerancia) and
                (x1_casa - tolerancia <= box_peca['x2'] <= x2_casa + tolerancia) and
                (y1_casa - tolerancia <= box_peca['y2'] <= y2_casa + tolerancia)
            ):
                localizacoes.append((peca, casa))
                encontrou = True
                break

        if not encontrou:
            localizacoes.append((peca, None))

    return localizacoes



        


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


resultados = mapping_bounding_box(dict_yolo_example, dicionario_kAnova)
for peca, casa in resultados:
    print(f"A peça {peca['name']} está localizada na casa {casa}")
    
    
