# Escreva um programa em python que gere uma matriz M[5][5] com números aleatórios entre 1 e 50
# A seguir, troque os elementos da diagonal principal com os elementos da diagonal secnudária
# Imprima a nova matriz

from random import randint
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = randint(1, 50)
        linha.append(valor)
    matriz.append(linha)
print("Matriz original:")
for linha in matriz:
    print(linha)

for i in range(5):
    matriz[i][i], matriz[i][4 - i] = matriz[i][4 - i], matriz[i][i]
print("Nova matriz:")
for linha in matriz:
    print(linha)