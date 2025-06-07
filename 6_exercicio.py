# Elabore um programa em python que gere uma matriz 5x5
# e calcule e mostre a diagonal principal e a secundária da matriz.
from random import randint

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = randint(1, 50)
        linha.append(valor)
    matriz.append(linha)
print("Matriz:")
for  linha in matriz:
    print(linha)
    
print("Diagonal principal:")
for i in range(5):
    print(matriz[i][i], end=' ')
    
print("\nDiagonal secundária:")
for i in range(5):
    print(matriz[i][4-i], end=' ')