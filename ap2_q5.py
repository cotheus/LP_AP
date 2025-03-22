lado1 = float(input('Forneça o primeiro lado: '))
lado2 = float(input('Forneça o segundo lado: '))
lado3 = float(input('Forneça o terceiro lado: '))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        if lado1 == lado2 and lado2 == lado3: print('O triângulo é equilátero.')
        else: print('O triângulo é isósceles.')
    else: print('O trinângulo é escaleno.')
else: print('Não é um triângulo.')