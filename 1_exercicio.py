# Faça um programa em python que leia uma matriz 2x3 de inteiros
# imprima a matriz e a soma dos elementos da matriz.
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor: [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

soma = 0
for i in range(2):
    for j in range(3):
        soma += matriz[i][j]
print(f"Soma dos elementos da matriz: {soma}")