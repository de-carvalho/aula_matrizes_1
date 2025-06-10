# Elabore um programa em python que leia duas matrizes A (mxn) e B (pxq)
# e calcule e mostre a matriz python que é a soma de A com B (caso a soma seja possível).
from random import randint

matriz_a = []
matriz_b = []
m, n = 3, 3
p, q = 3, 3

if m != p or n != q:
    print("A soma das matrizes não é possível, pois as dimensões não coincidem.")
else:
    for i in range(m):
        linha = []
        for j in range(n):
            valor = randint(1, 50)
            linha.append(valor)
        matriz_a.append(linha)

    for i in range(p):
        linha = []
        for j in range(q):
            valor = randint(1, 50)
            linha.append(valor)
        matriz_b.append(linha)

    print("Matriz A:")
    for linha in matriz_a:
        print(linha)

    print("\nMatriz B:")
    for linha in matriz_b:
        print(linha)

    matriz_soma = []
    for i in range(m):
        linha_soma = []
        for j in range(n):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha_soma.append(soma)
        matriz_soma.append(linha_soma)

    print("\nMatriz Soma (A + B):")
    for linha in matriz_soma:
        print(linha)