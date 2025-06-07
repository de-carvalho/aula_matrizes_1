# Faça um programa em python que gere uma matriz 10x10 de inteiros aleatórios entre 1 e 50
# imprima a matriz e o menor elemento de cada coluna
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

print("Menor elemento de cada coluna:")
for j in range(10):
    menor = min(matriz[i][j] for i in range(10))
    print(f"Menor elemento da coluna {j}: {menor}")