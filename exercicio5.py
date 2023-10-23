#crie um algoritmo que solicite que o usuario digite 4 notas
#elas precisam ser armazenadas em um vetor.
#some as notas, calcule a média, e mostre na tela a media final
# do aluno, se ele foi aprovado com nota maior ou igual a 7.
# ou se foi reprovado.

notas = [0]*4

for x in range(4):
    notas[x] = float (input(f'Digite sua {x+1}a nota: '))

media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

if media >= 7:
    print(f'Aluno aprovado! A média do aluno foi: {media}')

else:
    print(f'Aluno reprovado! A média do aluno foi: {media}')