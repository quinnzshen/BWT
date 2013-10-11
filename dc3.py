# Quinn Z Shen
# CS 176; dc3 implementation

import string
import radix

LEXICALGRAPHICAL_ALPHABET = '$' + string.ascii_uppercase + string.ascii_lowercase

def dc3(input):
    b_0, b_1, b_2 = [], [], []

    for i in xrange(len(input)):
        if (i % 3) == 0:
            b_0.append(i)
        elif (i % 3) == 1:
            b_1.append(i)
        elif (i % 3) == 2:
            b_2.append(i)   

    c = b_1 + b_2
    print "c"
    print c

    input.extend([0, 0]) # Ensure that each string is a triple
    r_1 = [tuple(input[x:x+3]) for x in b_1]
    r_2 = [tuple(input[x:x+3]) for x in b_2]
    input = input[:-2]

    r = r_1 + r_2

    print "r"
    print r

    r_prime = radix.radix_sort(r, max(input))

    print "r_prime"
    print r_prime

    a_dict = rank(r, r_prime)
    print "a_dict"
    print a_dict
    b_dict = {}
    counter = 0
    for x in c:
        b_dict[x] = a_dict[counter]
        counter += 1
    b_dict[len(input)] = 0
    b_dict[len(input) + 1] = 0
    print "b_dict"
    print b_dict

    b0_dict = {}
    for x in b_0:
        b0_dict[x] = (input[x], b_dict[x + 1])
    print "b0_dict"
    print b0_dict

    # if not(unique(r_prime)):
    #     r_prime = dc3(r_prime)

def unique(input):
    previous = None
    for x in input:
        if x == previous:
            return False
        previous = x
    return True

def rank(r, r_prime):
    counter = 0
    a_set = set()
    a_map = dict()
    r_prime_rank = []

    for x in r_prime:
        if not (x in a_set):
            a_set.add(x)
            counter += 1
            a_map[x] = counter

    print a_map

    for x in r:
        r_prime_rank.append(a_map[x])

    print "len(a_set)"
    print len(a_set)
    print "len(r)"
    print len(r)
    print "r_rank"
    print r_prime_rank

    if len(a_set) != len(r):
        print "~~~recursion~~~"
        # r_prime_suffix_array = dc3(r_rank)
        r_prime_suffix_array = [8, 0, 1, 6, 4, 2, 5, 3, 7][1:]
        a_dict = {r_prime_suffix_array[i]: (i + 1) for i in r_prime_suffix_array}
    else:
        a_dict = {i:r_prime_rank[i] for i in xrange(len(r_prime_rank))}
    
    return a_dict

    
    return 
    # previous = None
    # r_rank = []
    # r_prime_rank = []
    # for x in range(len(r_prime)):
    #     if r_prime[x] != previous:
    #         counter += 1
    #         previous = r_prime[x]
    #     r_prime_rank.append(counter)
    # print r_prime
    # print r_prime_rank

def to_integer_alphabet(string):
    character_set = set(x for x in string)
    character_mapping = {}
    for char in LEXICALGRAPHICAL_ALPHABET:
        if char in character_set:
            character_mapping[char] = len(character_mapping)
    return [character_mapping[i] for i in string]


def main():
    input_string = to_integer_alphabet("yabbadabbado$")
    print input_string
    dc3(input_string)

if __name__ == "__main__":
    main()