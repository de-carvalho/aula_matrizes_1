# Elabore um programa em python que gere uma matriz 4x6
# e calcule e mostre a sua matriz transposta equivalente.
from random import randint

matriz = []

for i in range(4):
    linha = []
    for j in range(6):
        valor = randint(1, 50)
        linha.append(valor)
    matriz.append(linha)
print("Matriz original:")

for linha in matriz:
    print(linha)
print("\nMatriz transposta:")
for j in range(6):
    for i in range(4):
        print(matriz[i][j], end=' ')
    print()