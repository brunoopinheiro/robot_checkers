from neural_network.yolo_test import Model, cv2
from neural_network.yolo_test import main


# (piece) [x2, y1, x1, y2]
a1 = [450, 140, 400, 90]
a3 = [450, 240, 400, 190]; a5 = [450, 290, 400, 240]; a7 = [450, 390, 400, 340]
b2 = [400, 190, 350, 140]; b4 = [400, 290, 350, 240]; b6 = [400, 390, 350, 340]; b8 = [400, 490, 350, 440]
c1 = [350, 140, 300, 90]; c3 = [350, 240, 300, 190]; c5 = [350, 290, 300, 240]; c7 = [350, 390, 300, 340]
d2 = [300, 190, 250, 140]; d4 = [300, 290, 250, 240]; d6 = [300, 390, 250, 340]; d8 =[300, 490, 250, 440]
e1 = [250, 140, 200, 90]; e3 = [250, 240, 200, 190]; e5 = [250, 340, 200, 290]; e7 = [250, 440, 200, 390]
f2 = [200, 190, 150, 140]; f4 = [200, 290, 150, 240]; f6 = [200, 390, 150, 340]; f8 = [200, 490, 150, 440]
g1 = [150, 140, 100, 90]; g3 = [150, 240, 100, 190]; g5 = [150, 340, 100, 290]; g7 = [150, 440, 100, 390]
h2 = [100, 190, 150, 50]; h4 = [100, 290, 150, 150]; h6 = [100, 390, 150, 250]; h8 = [100, 490, 150, 350]



meu_dicionario = {
    'a1': a1, 'a3': a3, 'a5': a5, 'a7': a7,
    'b2': b2, 'b4': b4, 'b6': b6, 'b8': b8,
    'c1': c1, 'c3': c3, 'c5': c5, 'c7': c7,
    'd2': d2, 'd4': d4, 'd6': d6, 'd8': d8,
    'e1': e1, 'e3': e3, 'e5': e5, 'e7': e7,
    'f2': f2, 'f4': f4, 'f6': f6, 'f8': f8,
    'g1': g1, 'g3': g3, 'g5': g5, 'g7': g7,
    'h2': h2, 'h4': h4, 'h6': h6, 'h8': h8
}


def coordenadas(dicionario_casas):
    for id, casa in dicionario_casas.items():
        soma = sum(casa)
        for indice in range(4):
            casa[indice] = casa[indice]/soma
    return dicionario_casas
                    
mapeadas = coordenadas(meu_dicionario)
print(mapeadas)


class Mapping:

    @staticmethod
    def mapping_bounding_boxes(dict_yolo):
        for casa in mapeadas.values():
            for chave, coordanada in casa:
                for coordanadas_yolo in dict_yolo.values():
                    for coordenada_yolo in coordanadas_yolo:
                        if coordanada >= coordenada_yolo*0.9 and coordanada <= coordanadas_yolo*1.1:
                            return coordanadas_yolo

    
    
if __name__ == "__main__":
    Mapping.mapping_bounding_boxes({main()})
        




# n_digitos = 14
# with open(f'docs/checkers_mapping.txt', 'w') as f:
#     conteudo = 'Checkers mapped'
#     for indice, casa in zip(range(32), mapeadas:
#         conteudo += f'\n{casa}'
#         for coordenada in mapeadas[indice]:
#             conteudo += '  ' +str(round(coordenada, n_digitos))
#     f.write(conteudo)

        

