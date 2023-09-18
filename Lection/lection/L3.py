# def sum_nubers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# a = sum_nubers(5)
# print(a)


# def sum_nubers(n, y = 'hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# a = sum_nubers(5, 'wqert')
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res +=i
#     return res

# print(sum_str('q','w','e'))
# print(sum_str('q','w','e', '21', '231'))

# ИМПОРТ (МОДУЛЬ)

# import modul
# print(modul.max1(5,9))

# from modul import max1
# print(max1(10,9))

# from modul import *
# print(max1(10,9))


# import modul as m1
# print(m1.max1(5,9))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range (1,10):
#     list_1.append(fib(i))
# print(list_1)


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = right[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [1,2,3,1,4,21,45,1,431,1,22,4,45,1,2]
# merge_sort(list1)
# print(list1)
