# Elabore um progragama em pyhton que declare uma matriz quadrade de 10 linnhas por 10 colunas
# e verifique se a matriz é siméttrica em relação a diagonal principal.
# A matriz simétrica é aquela em que todos os elementos A(i, j) = A(j, i) para quaisquer valores de i e j.
# Assim, A[2, 1] deverá ser igual a A[1, 2] e A [3, 5] deverá ser igual a A[5, 3].
# Imprimir mensagem "Matriz simétrica" ou "Matriz não simétrica".

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
simetrica = True
for i in range(10):
    for j in range(10):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break
if simetrica:
    print("Matriz simétrica")
else:
    print("Matriz não simétrica")