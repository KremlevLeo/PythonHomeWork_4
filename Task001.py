import random

num = int(input("Введите какое колличчество чисел должно быть в списке: "))
llist = []
amount = 0
for i in range(num):
    llist.append(random.randrange(0,10))
    if i % 2 != 0:
        amount += llist[i]
print(f'{llist} -> {amount}')
