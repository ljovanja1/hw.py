# def f(x):
#     return x*x

# a = f
# print(type(a))
# print(a(5))
# print(f(5))


# def calk1(a, b):
#     return a + b


# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))
     
# math(calk1, 5, 45)
# math(calk2, 5, 45)

# ЛЯМДА
# calk1 =  lambda a,b: a + b 
# calk2 =  lambda a,b: a * b
 
# math(lambda a,b: a + b, 5, 45)
# math(lambda a,b: a * b, 5, 45)


# data = [1,2,3,4,5,8,15,23,38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
        
# print(res)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]
# data = [1,2,3,4,5,8,15,23,38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x%2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# def where(f, col):
#     return[x for x in col if f(x)]
# data = [1,2,3,4,5,8,15,23,38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x%2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# data = ' 14 412 4124 55 1'
# print(data)
# # data = data.split()
# # print(data)
# data = list(map(int, data.split()))
# print(data)


# data = [15, 65, 9, 56, 75]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res) 


