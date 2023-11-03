#Faça um código que receba 4 números e realize a soma deles e a média entre eles. e mostre os resultados.

soma = 0

for x in range(4):
    numero = float(input('Digite um número: '))
    soma += numero

media = soma / 4

print(f'A soma dos números são {soma}')
print(f'A média dos números são {media}')


