a = [0]*5

for i in range(5):
    a[i]=[0]*5
    for j in range(5):
        if (i==j or i+j==4):
            a[i][j] = 1
print('Matriz gerada:')
for i in range(5):
    print(a[i])