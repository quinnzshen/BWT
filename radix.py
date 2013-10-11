from math import log
 
def getDigit(num, base, digit_num):
    # pulls the selected digit
    return (num // base ** digit_num) % base  
 
def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [ [] for i in range(size) ]  
 
def split(a_list, base, index):
    buckets = makeBlanks(base + 1)
    for num in a_list:
        buckets[num[index]].append(num)  
    return buckets
 
# concatenate the lists back in order for the next step
def merge(a_list): 
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list
 
def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)  
 
def radix_sort(a_list, base):
    # there are as many passes as there are digits in the longest number
    passes = 3
    new_list = list(a_list)
    for index in range(passes)[::-1]:
        new_list = merge(split(new_list, base, index))
    return new_list