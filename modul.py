def max1(a,b):
    if a > b:
        return a
    return b

def min_max_serch(lst):
    min = lst[0]
    max = lst[0]
    for num in lst[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max


def change(minN, maxN, lst):
    for i in range(len(lst)):
        if lst[i] == maxN:
            lst[i] = minN
    return lst



def serch_num(num: int) -> bool:
    flag = True
    if num % 2 == 0 and num != 2:
        return False
    
    for i in range(3, num):
        if num % i == 0:
            return False
    return True
        