f = [1, 1]
n = int(input())
for i in range(2, n):
    f.append(f[i-1] + f[i-2])

for i in range(n):
    print(f[i], end=" ")
