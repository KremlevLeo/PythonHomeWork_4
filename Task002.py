import random

num_A = int(input("\nВведите какое колличчество списков должно быть в списке: "))
num_B = int(input("Введите какое колличчество эллементов должно быть в подсписках: "))
llist = [[0] * num_B for i in range(num_A)]
llist_mean = []

for i in range(len(llist)):
    arith_mean = 0
    for c in range(len(llist[i])):
        llist[i][c] = int(random.randrange(0,11))
        arith_mean += llist[i][c]
    llist_mean.append(arith_mean/num_B)

print(f'\nДвумерный список: {llist}')
print('\nСреднее арифметическое подсписков:')
for i in range(len(llist)):
    print(f'{i+1}) {llist[i]} -> {llist_mean[i]}')