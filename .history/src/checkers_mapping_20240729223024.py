from math import pi, sin



# (piece) [x2, y1, x1, y2]
a1 = [552, 30, 502, 81]
a3 = [0]*4; a5 = [0]*4; a7 = [0]*4
b2 = [0]*4; b4 = [0]*4; b6 = [0]*4; b8 = [0]*4
c1 = [0]*4; c3 = [0]*4; c5 = [0]*4; c7 = [0]*4
d2 = [0]*4; d4 = [0]*4; d6 = [0]*4; d8 = [0]*4
e1 = [0]*4; e3 = [0]*4; e5 = [0]*4; e7 = [0]*4
f2 = [0]*4; f4 = [0]*4; f6 = [0]*4; f8 = [0]*4
g1 = [0]*4; g3 = [0]*4; g5 = [0]*4; g7 = [0]*4
h2 = [0]*4; h4 = [0]*4; h6 = [0]*4; h8 = [0]*4



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

largura_horizontal = 553-153
largura_vertical = 430-30
degree_vertical = 90-88.69
degree_horizonal = 180-178.16

cateto_oposto_y = sin((pi/180)*degree_horizonal)*largura_horizontal

cateto_oposto_x = sin((pi/180)*degree_vertical)*largura_vertical

def coordenadas(casa_a1, dicionario_casas):
    shift_x = 50
    for a in list('a3', 'a5', 'a7'):
        dicionario_casas[a][0] = dicionario_casas['a1'][0]+shift_x
        shift_x += 50
    for b, a in zip(list('b2', 'b4', 'b6', 'b8'), list('a1','a3', 'a5', 'a7')):
        if b == 'b8':
            k = 50
        else:
            k = 0
        dicionario_casas[b][0] = dicionario_casas[a][2]
        dicionario_casas[b][2] = dicionario_casas[a][0]+k
    for c, b in zip(list('c1', 'c3', 'c5', 'c7'), list('b2', 'b4', 'b6', 'b8')):
        dicionario_casas[c][0] = dicionario_casas[b][2]
        dicionario_casas[c][2] = dicionario_casas[b][0]
    for d, c in zip(list('d2', 'd4', 'd6', 'd8'), list('c1', 'c3', 'c5', 'c7')):
        if d == 'd8':
            k = 50
        else:
            k = 0
        dicionario_casas[d][0] = dicionario_casas[c][2]
        dicionario_casas[d][2] = dicionario_casas[c][0]+k
    for e, d in zip(list('e1', 'e3', 'e5', 'e7'), list('d2', 'd4', 'd6', 'd8')):
        dicionario_casas[e][0] = dicionario_casas[d][2]
        dicionario_casas[e][2] = dicionario_casas[d][0]
    for f, e in zip(list('f2', 'f4', 'f6', 'f8'), list('e1', 'e3', 'e5', 'e7')):
        if f == 'f8':
            k = 50
        else:
            k = 0
        dicionario_casas[f][0] = dicionario_casas[e][2]
        dicionario_casas[f][2] = dicionario_casas[e][0]+k
    for g, f in zip(list('g1', 'g3', 'g5', 'g7'), list('f2', 'f4', 'f6', 'f8')):
        dicionario_casas[f][0] = dicionario_casas[d][2]
        dicionario_casas[e][2] = dicionario_casas[d][0]
    
    
    for i in dicionario_casas:
        soma = sum(i)
        for indice in range(4):
            i[indice] = i[indice]/soma
    return dicionario_casas
                    
mapeadas = coordenadas(a1, meu_dicionario)
print(mapeadas)

dicionario_casas = ['a1', 'a3', 'a5', 'a7', \
               'b2', 'b4', 'b6', 'b8', \
                'c1', 'c3', 'c5', 'c7', \
                'd2', 'd4', 'd6', 'd8', \
                'e1', 'e3', 'e5', 'e7', \
                'f2', 'f4', 'f6', 'f8', \
                'g1', 'g3', 'g5', 'g7', \
                'h2', 'h4', 'h6', 'h8', \
    ]
n_digitos = 14
with open(f'docs/checkers_mapping.txt', 'w') as f:
    conteudo = 'Checkers mapped'
    for indice, casa in zip(range(32), dicionario_casas):
        conteudo += f'\n{casa}'
        for coordenada in mapeadas[indice]:
            conteudo += '  ' +str(round(coordenada, n_digitos))
    f.write(conteudo)

        

