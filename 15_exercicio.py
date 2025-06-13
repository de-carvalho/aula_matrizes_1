from random import randint

matriz = []

for i in range(9):
    linha = []
    for j in range(9):
        numero = randint(0, 10)
        linha.append(numero)
    matriz.append(linha)

print("Matriz completa:")
for linha in matriz:
    print(linha)

q = input("Escolha um quadrante (1, 2, 3 ou 4): ")

if q == '1':
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()
elif q == '2':
    for i in range(4):
        for j in range(5, 9):
            print(matriz[i][j], end=' ')
        print()
elif q == '3':
    for i in range(5, 9):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()
elif q == '4':
    for i in range(5, 9):
        for j in range(5, 9):
            print(matriz[i][j], end=' ')
        print()
else:
    print("Número inválido. Tente 1, 2, 3 ou 4.")
