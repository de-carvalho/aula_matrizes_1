# Faça um programa em python que gere uma matriz 10x10 de inteiros aleatórios entre 1 e 50
# Imprima a matriz e a média de todos os elementos da matriz.

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

soma = 0
for i in range(10):
    for j in range(10):
        soma += matriz[i][j]
media = soma / (10 * 10)
print(f"Média dos elementos da matriz: {media}")