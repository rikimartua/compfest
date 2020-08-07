n = 4
q = 2
pendaftar = ["dengklek", "chanek", "ganesh", "blangkon"]
antri = ["chanek", "ganesha"]
result = []
for i in range(0, q):
    for j in range(0, n):
        if antri[i] == pendaftar[j]:
            result.append(j+1)
        else:
            result.append("-1")

print(result)
