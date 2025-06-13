from random import randint

notas = []

for i in range(10):
    atleta = []

    for j in range(5):
        nota = randint(0, 10)
        atleta.append(nota)
    notas.append(atleta)

print("Notas dos atletas:")
for atleta in notas:
    print(atleta)

medias = []

for atleta in notas:
    notas_ordenadas = sorted(atleta)
    notas_validas = notas_ordenadas[1:-1]
    media = sum(notas_validas) / 3
    medias.append(media)

print("Médias:")
for i in range(10):
    print("Atleta", i + 1, "teve média", round(medias[i], 2))

maior_media = max(medias)
vencedor = medias.index(maior_media) + 1
print("O atleta que ganhou foi o número", vencedor, "com média", round(maior_media, 2))
