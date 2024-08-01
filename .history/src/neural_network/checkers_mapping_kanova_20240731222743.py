
a1 = [90, 30, 140, 80]; a3 = [190, 30, 240, 80]; a5 = [290, 30, 340, 80]; a7 = [390, 30, 440, 80]
b2 = [140, 80, 190, 130]; b4 = [240, 80, 290, 130]; b6 = [340, 80, 390, 130]; b8 = [440, 80, 490, 130]
c1 = [90, 130, 140, 180]; c3 = [190, 130, 240, 0]; c5 = [290, 0, 340, 0]; c7 = [390, 0, 440, 0]
d2 = [140, 0, 190, 0]; d4 = [240, 0, 290, 0]; d6 = [340, 0, 390, 0]; d8 =[440, 0, 490, 0]
e1 = [90, 0, 140, 0]; e3 = [190, 0, 240, 0]; e5 = [290, 0, 340, 0]; e7 = [390, 0, 440, 0]
f2 = [140, 0, 190, 0]; f4 = [240, 0, 290, 0]; f6 = [340, 0, 390, 0]; f8 = [440, 0, 490, 0]
g1 = [90, 0, 140, 0]; g3 = [190, 0, 240, 0]; g5 = [290, 0, 340, 0]; g7 = [390, 0, 440, 0]
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
