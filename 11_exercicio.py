# Escreva um programa em python que gere uma matriz M[10][10] com números aleatórios entre 1 e 50
# e copie um vetor de 10 elementos, os números da diagonal principal
# Imprima a matriz e o vetor

from random import randint
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        valor = randint(1, 50)
        linha.append(valor)
    matriz.append(linha)
print("Matriz:")
for linha in matriz:
    print(linha)
vetor = []
for i in range(10):
    vetor.append(matriz[i][i])
print("Vetor da diagonal principal:")
print(vetor)