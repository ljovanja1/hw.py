'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию
.split()'''

# new = "a a a b c a a d c d d".split()
# print(new)
# dict_1 = {}

# for letter in new:
#     if  letter in dict_1:
#         dict_1[letter] += 1
#         print(letter + "_" + str(dict_1[letter]), end = " ")
#     else:
#         dict_1[letter] = 0
#         print(letter, end = " ")
        
# # без пробела на конце 
# new = "a a a b c a a d c d d".split()
# print(new)
# dict_1 ={}
# for letter in new[:-1]:
#     if letter in dict_1:
#         dict_1[letter] += 1
#         print(letter + "_" + str(dict_1[letter]), end = " ")
#     else:
#         dict_1[letter] = 0
#         print(letter, end = " ")
# if new[-1] in dict_1:
#     dict_1[new[-1]] += 1
#     print(new[-1] + "_" + str(dict_1[new[-1]]))
# else:
#     dict_1[new[-1]] = 0
#     print(new[-1])

# # решение через сплит
# string = input('Enter the string:')
# new = string.split()

# for i in range(len(new)):
#     count = 1
#     for j in range(i + 1, len(new)):
#         if new[i] == new [j]:
#             count += 1
#             new[j] = new[j] + '_' + str(count)
#         if count > 1:
#             new[i] = new[i] + '_' + str(count)
            
# print(''.join(new))

# # вариант с переменной:

# s='a a a b c a a d c d d'.split()
# print(s)
# s2=''
# dict={}

# for item in s:
#     if item in dict:
#         dict[item]+=1
#         s2+=item+'_'+str(dict[item])+' '
#         #print(f"{item}_{dict[item]}", end=' ')
#     else:
#         dict[item]=0
#         s2+=item+' '
#         #print(f"{item}", end=' ')
# print(s2.strip())
