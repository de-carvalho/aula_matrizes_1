# Faça um programa em python que gere as 5 notas (de 0 a 10) de 10 atletas em uma competição
# Armazene em uma matriz de 10x5.
# Após, calcule a média de cada atleta descartando a maior e menor nota obtida
# E diga qual atleta venceu a comptição, ou seja, o número da linha

from random import randint
matriz = []
for i in range(10):
    linha = []
    for j in range(5):
        valor = randint(0, 10)
        linha.append(valor)
    matriz.append(linha)
print("Matriz de notas:")
for linha in matriz:
    print(linha)
medias = []
for i in range(10):
    atleta = matriz[i]
    maior_nota = max(atleta)
    menor_nota = min(atleta)
    atleta.remove(maior_nota)
    atleta.remove(menor_nota)
    media = sum(atleta) / len(atleta)
    medias.append(media)
print("Médias dos atletas:")
for i, media in enumerate(medias):
    print(f"Atleta {i + 1}: {media:.2f}")
vencedor = medias.index(max(medias)) + 1
print(f"O atleta vencedor é o número {vencedor} com média {medias[vencedor - 1]:.2f}")