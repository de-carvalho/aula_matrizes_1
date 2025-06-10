# Elabore um programa em python que gere uma matriz aleatoria (9x9)
# com números entre 0 e 10, imprima-a
# Após, peça quadrante desejado e imprima os elementos desse quadrante

from random import randint

matriz = []
for i in range(9):
    linha = []
    for j in range(9):
        valor = randint(0, 10)
        linha.append(valor)
    matriz.append(linha)
print("Matriz original:")
for linha in matriz:
    print(linha)
quadrante = input("Informe o quadrante desejado (1, 2, 3 ou 4): ")
if quadrante == '1':
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()
elif quadrante == '2':
    for i in range(4):
        for j in range(5, 9):
            print(matriz[i][j], end=' ')
        print()
elif quadrante == '3':
    for i in range(5, 9):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()
elif quadrante == '4':
    for i in range(5, 9):
        for j in range(5, 9):
            print(matriz[i][j], end=' ')
        print()
else:
    print("Quadrante inválido. Por favor, escolha entre 1, 2, 3 ou 4.")