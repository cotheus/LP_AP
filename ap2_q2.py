print('Este programa seleciona o maior número de três números fornecidos pelo usuário ')
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))
if valor1 >= valor2:
    if valor1 > valor3: print(f'O {valor1} é o maior dos três.')
    else: print(f'O {valor3} é o maior dos três.')
elif valor2 >= valor1:
    if valor2 > valor3: print(f'O {valor2} é o maior dos três.')
    else: print(f'O {valor3} é o maior dos três.')