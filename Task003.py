import random

llist = []
for i in range(30):
    llist.append(random.randrange(0,30))

print(f'\nИзначальный список: {llist}')

for i in range(len(llist)-1):
    smallest = i
    for j in range (i+1, len(llist)):
        if llist[j] < llist[smallest]:
            smallest = j
    llist[i], llist[smallest] = llist[smallest], llist[i]

print(f'\nОтсортированный список: {llist}')