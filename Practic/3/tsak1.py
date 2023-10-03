# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_1 = []

for _ in range(5):
    list_1.append(input('введите число '))

my_set = set(list_1) # set() - убирает дубли
print(*my_set)
print (len(my_set))