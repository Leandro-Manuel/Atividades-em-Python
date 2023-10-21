#crie um algoritmo que receba 3 números e informe qual o maior entre eles.

numero1 = int (input('Digite um número: '))
numero2 = int (input('Digite outro número: '))
numero3 = int (input('Digite outro número: '))

if numero1 > numero2:
    print(f'{numero1} é o maior!')
elif numero2 > numero3:
    print(f'{numero2} é o maior!')

else:
    print(f'{numero3} é o naior!')


