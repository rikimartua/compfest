entry = input().split(' ')
r = entry[0]
c = entry[1]
keuntungan = []
hasil = 0
for i in range(0, int(r)):
    entry = input().split(' ')
    keuntungan += entry

for i in range(0, len(keuntungan)):
    hasil += int(keuntungan[i])

print(hasil)

