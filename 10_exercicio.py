import random

matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randint(1, 50))
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

numero_linha = int(input("Escolha uma linha (0 a 9): "))

vetor = matriz[numero_linha]

print("Vetor com os números da linha escolhida:")
print(vetor)
