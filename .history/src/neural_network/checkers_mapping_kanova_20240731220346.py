
a1 = [90, 0, 140, 0]; a3 = [190, 0, 240, 0]; a5 = [290,0,340,0]; a7 = [340, 340, 444, 390]
b2 = [350, 141, 400, 191]; b4 = [348, 241, 398, 291]; b6 = [346, 341, 396, 391]; b8 = [344, 441, 394, 491]
c1 = [90, 92, 350, 142]; c3 = [348, 192, 298, 242]; c5 = [346, 242, 296, 292]; c7 = [344, 342, 294, 392]
d2 = [250, 143, 300, 193]; d4 = [248, 243, 298, 293]; d6 = [246, 343, 396, 293]; d8 =[244, 443, 294, 493]
e1 = [200, 144, 250, 94]; e3 = [198, 244, 248, 194]; e5 = [196, 344, 246, 294]; e7 = [144, 444, 244, 394]
f2 = [150, 145, 200, 195]; f4 = [148, 245, 198, 295]; f6 = [146, 345, 196, 395]; f8 = [144, 445, 194, 495]
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
