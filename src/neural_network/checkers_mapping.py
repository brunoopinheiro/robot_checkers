
# (piece) [x2, y1, x1, y2]
a1 = [450, 140, 400, 90]; a3 = [448, 240, 398, 190]; a5 = [446, 290, 396, 240]; a7 = [444, 390, 394, 340]
b2 = [400, 191, 350, 141]; b4 = [398, 291, 348, 241]; b6 = [396, 391, 346, 341]; b8 = [394, 491, 344, 441]
c1 = [350, 142, 300, 92]; c3 = [348, 242, 298, 192]; c5 = [346, 292, 296, 242]; c7 = [344, 392, 294, 342]
d2 = [300, 193, 250, 143]; d4 = [298, 293, 248, 243]; d6 = [296, 393, 246, 343]; d8 =[294, 493, 244, 443]
e1 = [250, 144, 200, 94]; e3 = [248, 244, 198, 194]; e5 = [246, 344, 196, 294]; e7 = [244, 444, 144, 394]
f2 = [200, 195, 150, 145]; f4 = [198, 295, 148, 245]; f6 = [196, 395, 146, 345]; f8 = [194, 495, 144, 445]
g1 = [150, 146, 100, 96]; g3 = [148, 246, 98, 196]; g5 = [146, 346, 96, 296]; g7 = [144, 446, 94, 396]
h2 = [100, 197, 50, 147]; h4 = [98, 297, 48, 247]; h6 = [96, 397, 46, 347]; h8 = [94, 497, 44, 447]



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
    for casa in dicionario_casas.values():
        soma = sum(casa)
        for i in range(4):
            casa[i] = casa[i]/soma
    return dicionario_casas
                    
mapeadas = coordenadas(meu_dicionario)
print(mapeadas)

        

lista_casas = ['a1','a3','a5','a7', \
    'b2','b4', 'b6', 'b8', \
    'c1','c3','c5','c7', \
    'd2','d4', 'd6','d8', \
    'e1','e3','e5', 'e7', \
    'f2', 'f4', 'f6', 'f8', \
    'g1', 'g3', 'g5', 'g7', \
    'h2', 'h4', 'h6', 'h8']


n_digitos = 5
with open(f'docs/checkers_mapping.txt', 'w') as f:
    conteudo = ''
    for notacao_casa, casa in zip(lista_casas, mapeadas.values()):
        conteudo += f'\n{notacao_casa}'
        for coordenada in casa:
            conteudo += '  ' +str(round(coordenada, n_digitos))
    f.write(conteudo)
    
