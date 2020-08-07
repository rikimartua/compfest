entry = input().split(' ')
average = 0
for i in range(0, len(entry)):
    average += int(entry[i])
print(average / len(entry))
