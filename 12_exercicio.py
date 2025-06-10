# Faça um programa em python que gere uma matriz 5x5 com valores entre 1 e 50
# Imprima a matriz e troque uma linha por outra linha informada pelo usuário
# Mostre a matriz após a troca

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
linha1 = int(input("Informe o número da primeira linha (0 a 4): "))
linha2 = int(input("Informe o número da segunda linha (0 a 4): "))
# Troca as linhas
matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]
print("Matriz após a troca:")
for linha in matriz:
    print(linha)