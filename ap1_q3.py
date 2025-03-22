import math
x1 = int(input('Forneça o x1: '))
y1 = int(input('Forneça o y1: '))
x2 = int(input('Forneça o x2: '))
y2 = int(input('Forneça o y2: '))
distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f'P({x1}, {y1}); Q({x2}, {y2})')
print(f'A distância entre os dois pontos é {distancia}.')
