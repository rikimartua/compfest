entry = input()
queue = []

for i in range(0, int(entry)):
    entry1 = input().split(' ')
    if entry1[0] == '1':
        queue.append(entry1[1])
    else:
        print(queue[0])
        queue.pop(0)
