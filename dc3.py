# Quinn Z Shen
# CS 176; dc3 implementation

import radix

def dc3(input):
    print radix.radix_sort(list(set(i for i in input)), 10)
    b_0, b_1, b_2 = [], [], []

    for i in xrange(len(input)):
        if (i % 3) == 0:
            b_0.append(i)
        elif (i % 3) == 1:
            b_1.append(i)
        elif (i % 3) == 2:
            b_2.append(i)   

    c = b_1 + b_2

    input += "$$" #To ensure that each string is a triple towards the end.
    r_1 = [input[x:x+3] for x in b_1]
    r_2 = [input[x:x+3] for x in b_2]
    input = input[:-2] #TODO: More efficient method?

    r = r_1 + r_2

    r_prime = radix.radix_sort(r, len(set(list(r))))
    print r_prime

    # print rank(radix_sort(r), r)



def rank(input, r):
    rank_ref = dict()
    rank = 1
    output = []
    for i in input:
        if not(i in rank_ref):
            rank_ref[i] = rank
            rank += 1
    for i in r:
        output.append(rank_ref[i])
    return output

# def split(input, digit_num):
#     tmp = set()
#     unique_chars = []
#     for x in input:
#         if not(x[digit_num] in tmp):
#             tmp.add(x[digit_num])
#             unique_chars.append(x[digit_num])
#     unique_chars.sort()

#     bucket_ref = dict(zip(unique_chars, [x for x in range(len(unique_chars))]))
#     buckets = [[] for x in range(len(unique_chars))]
#     for char in input:
#         buckets[bucket_ref[char[digit_num]]].append(char)
#     return buckets

# def merge(input):
#     output = []
#     for sublist in input:
#         output.extend(sublist)
#     return output

# def radix_sort(input):
#     passes = 3
#     output = input
#     for i in range(passes)[::-1]:
#         output = merge(split(output, i))
#     return output

def main():
    dc3("yabbadabbado")

if __name__ == "__main__":
    main()