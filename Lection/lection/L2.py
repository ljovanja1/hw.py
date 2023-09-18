# list_1 = [] - # создание пустого списка
# list_2 = list() # создание пустого списка
# list_1 = [1,2,3,4,5,6,8,9] # список(это массив)

# вывод данных начинается с 0
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*list_1)
# print(list_1)

# for i in list_1:
#     print(i)
    
# print(len(list_1))
# print(list_1[8])
# print(list_1[-1])
# print(list_1)
# list_1.append(88) - добавляет 4
# print(list_1)


# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# # удаление последнего эллемента
# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()
# print(a) # 0
# print(list_1.pop()) # 0
# print(list_1) 
# print(list_1.pop())
# print(list_1)

# удаление конкретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(1))
# print(list_1)

# добавление в список на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # на элемент(2) вставляем  число (11)
# print(list_1) 


# срезы
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1])
# print(list_1[-1])
# print(list_1[:2])
# print(list_1[len(list_1)-2:])
# print(list_1[2:8])
# print(list_1[6:-18])


# # кортежи - неизменный список

# t = () # пустой кортеж
# print(type(t))

# t = (1,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))


# # a = 1
# # b = 2
# # a, b = 1, 2

# a,b,c = v
# print(a,b,c)

# t = (1,2,3,4,5)
# print(t[1])

# for i in range(len(t)):
#     print(t[i])

# t = [1,2,3,4,5]
# t[0] = 2

# print(t)

# # СЛОВАРИ
# d = {} #- создали пустой словарь
# d = dict() #- создали пустой словарь

# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'qewrty'
# print(d['q'])
# dic = {}
# # dic = {'up': '/', 'left' : '//', 'down' : '///', 'rught' : '////'}
# # del dic['left'] # удаление элемента
# # for item in dic:
# #     print('{}:{}'.format(item, dic[item]))
    
# # dic[895] = 7890
# # print(dic)

# dic = {'up': '/', 'left' : '//', 'down' : '///', 'rught' : '////'}
# print(dic.items())
# # for (k,v) in dic.items():
# #     print(k, v)


# Множества 

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')  # добавить (add)
# print(colors)
# colors.remove('red')  # убрать (remove)
# print(colors)
# # colors.remove('red')
# colors.discard('red')  #проверкаа значения и удаление (discard)
# print(colors)
# colors.clear()
# print(colors)

# операции со множествами питон
# a = {1,2,3,4,5,8}
# b = {2,5,8,13,21}
# c = a.copy() # копирование
# print(c)
# u = a.union(b)  # обьединение 
# print(u)
# i = a.intersection(b) # пересечение в обоих множествах
# print(i)
# dl = a.difference(b) # разность a от b
# print(dl)
# dr = b.difference(a) # разность b от a
# print(dr)
# q = a.union(b).difference(a.intersection(b)) # обьединение, разность a от b, пересечение в обоих множествах
# print(q)


# замороженное множество
# a = {1,8,4}
# b = frozenset(a)
# print(b)


# list_1 = [i for i in range(1,101) if i % 2 == 0]
# list_1 = [(i,i) for i in range(1,101) if i % 2 == 0]
# list_1 = [i*2 for i in range(10) if i % 2 == 0]
# print(list_1)
