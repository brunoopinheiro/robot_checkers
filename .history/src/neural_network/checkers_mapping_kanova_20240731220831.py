
a1 = [90, 0, 140, 0]; a3 = [190, 0, 240, 0]; a5 = [290, 0, 340, 0]; a7 = [340, 0, 390, 0]
b2 = [350, 0, 400, 0]; b4 = [348, 0, 398, 0]; b6 = [346, 0, 396, 0]; b8 = [344, 0, 394, 0]
c1 = [90, 0, 140, 0]; c3 = [190, 0, 240, 0]; c5 = [290, 0, 340, 0]; c7 = [340, 0, 390, 0]
d2 = [250, 0, 300, 0]; d4 = [248, 0, 298, 0]; d6 = [246, 0, 396, 0]; d8 =[244, 0, 294, 0]
e1 = [90, 0, 140, 0]; e3 = [190, 0, 240, 0]; e5 = [196, 0, 246, 0]; e7 = [144, 0, 244, 0]
f2 = [150, 0, 200, 0]; f4 = [148, 0, 198, 0]; f6 = [146, 345, 196, 395]; f8 = [144, 445, 194, 495]
g1 = [100, 96, 150, 146]; g3 = [98, 196, 148, 246]; g5 = [96, 296, 146, 346]; g7 = [94, 396, 144, 446]
h2 = [50, 147, 100, 197]; h4 = [48, 247, 98, 297]; h6 = [46, 347, 96, 397]; h8 = [44, 447, 94, 497]



dicionario_kAnova = {
    'a1': a1, 'a3': a3, 'a5': a5, 'a7': a7,
    'b2': b2, 'b4': b4, 'b6': b6, 'b8': b8,
    'c1': c1, 'c3': c3, 'c5': c5, 'c7': c7,
    'd2': d2, 'd4': d4, 'd6': d6, 'd8': d8,
    'e1': e1, 'e3': e3, 'e5': e5, 'e7': e7,
    'f2': f2, 'f4': f4, 'f6': f6, 'f8': f8,
    'g1': g1, 'g3': g3, 'g5': g5, 'g7': g7,
    'h2': h2, 'h4': h4, 'h6': h6, 'h8': h8
}


print(dicionario_kAnova)

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
    for notacao_casa, casa in zip(lista_casas, dicionario_kAnova.values()):
        conteudo += f'\n{notacao_casa}'
        for coordenada in casa:
            conteudo += '  ' +str(round(coordenada, n_digitos))
    f.write(conteudo)
