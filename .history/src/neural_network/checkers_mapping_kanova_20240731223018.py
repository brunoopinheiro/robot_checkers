
a1 = [90, 30, 140, 80]; a3 = [190, 30, 240, 80]; a5 = [290, 30, 340, 80]; a7 = [390, 30, 440, 80]
b2 = [140, 80, 190, 130]; b4 = [240, 80, 290, 130]; b6 = [340, 80, 390, 130]; b8 = [440, 80, 490, 130]
c1 = [90, 130, 140, 180]; c3 = [190, 130, 240, 180]; c5 = [290, 130, 340, 180]; c7 = [390, 130, 440, 180]
d2 = [140, 180, 190, 230]; d4 = [240, 180, 290, 230]; d6 = [340, 180, 390, 230]; d8 =[440, 180, 490, 230]
e1 = [90, 230, 140, 280]; e3 = [190, 230, 240, 280]; e5 = [290, 230, 340, 280]; e7 = [390, 230, 440, 280]
f2 = [140, 280, 190, 330]; f4 = [240, 280, 290, 330]; f6 = [340, 280, 390, 330]; f8 = [440, 280, 490, 330]
g1 = [90, 330, 140, 380]; g3 = [190, 330, 240, 0]; g5 = [290, 0, 340, 0]; g7 = [390, 0, 440, 0]
h2 = [140, 0, 190, 0]; h4 = [240, 0, 290, 0]; h6 = [340, 0, 390, 0]; h8 = [440, 0, 490, 0]



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
