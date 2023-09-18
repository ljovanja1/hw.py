# print(5)
# n = 5
# print(n)
# n = 1.89
# print(n)

# n = 'fdsfd'
# print(n)
# n1 = 'cscds'
# print(n1)

# n = 5 
# print(type(n))
# n='fw\ "s"f'
# print(type(n))

# a = 5
# b = 5.89
# c= 'hello'

# print(a,' - ', b, c)
# print(f"{a}, {b}, {c}")
# print("{} - {} - {}".format(a, b, c))


# print("import size")
# a = input()
# print(a)
# b = input("import 2size")

# print (a, '+', b, ' = ', a + b)


# c = 5.89
# print(c)
# print(type(c))
# n = str(c)
# n = bool(c)
# print(n)
# print(type(n))

# print("import size")
# a = int(input())
# b = int(input("import 2size"))
# print (a, '+', b, ' = ', a + b) - получаем сумму а не строку


# a = 4.123
# b = 6.213
# print(round(a*b,3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5


# a = 1 > 4
# print(a) # False
# # —------------------------------------
# a = 1 < 4 and 5 > 2
# print(a) # True
# # —------------------------------------
# a = 1 == 2
# print(a) # False
# # —------------------------------------
# a = 1 != 2
# print(a) # True
# # —------------------------------------
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# # —------------------------------------
# a = 1 < 3 < 5 < 10
# print (a) # True

# ЦИКЛЫ



# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i += 1
# else:
#     print('пожалуй')
#     print('хватит')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# ЦИКЛ FOR

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)


# a = 'asfasd'
# print(a[2])
# for i in a:
#     print(i)
    
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
    

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# СРЕЗЫ

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # k
print(text[-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ