print('Esse programa serve para calcular o seu peso ideal.')
sexo = input("Qual o seu sexo? Digite 'm' para masculino e 'f' para feminino: ")
if sexo == 'm' or sexo == 'f': altura = float(input('Digite a sua altura: '))
else: print('Sexo inválido')
if sexo == 'm':
    peso = 72.7 * altura - 58
    print(f'O seu peso ideal é {peso}')
elif sexo == 'f':
    peso = 62.1 * altura - 44.7
    print(f'O seu peso ideal é {peso}')
