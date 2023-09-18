a = int(input('Введите число a \n'))
b = int(input('Введите числ b \n'))

def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b-1)

res = f(a, b)
print(res)


# sum(2, 2)
# # 4

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a-1, b+1)


print(sum(a, b))