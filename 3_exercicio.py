# Faça um programa em python que gere uma matriz 10x10 de inteiros aleatórios entre 1 e 50
# imprima a matriz e a soma de todos os elementos em cada linha:

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
soma_linhas = []
for i in range(10):
    soma = 0
    for j in range(10):
        soma += matriz[i][j]
    soma_linhas.append(soma)
    print(f"Soma dos elementos da linha {i}: {soma}")
print("Soma de todos os elementos em cada linha:", soma_linhas)