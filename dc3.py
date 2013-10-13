# Quinn Z Shen
# CS 176 

import argparse
import string
import radix
import sys

LEXICALGRAPHICAL_ALPHABET = '$' + string.ascii_uppercase + string.ascii_lowercase

def read_file(file_name):
    # Open file
    f = open(file_name, 'r')

    text = ''
    sequences = []

    for line in f.readlines():
        line = line.rstrip()
        if line[0] == ">":
            sequences.append(text)
            text = ''
        else:
            text += line
    sequences.append(text)
    return sequences

def write_file(file_name, output_str):
    lines = []
    for i in range(1 + (len(output_str) - 1) // 80):
        lines.append(output_str[i * 80:(i + 1) * 80])

    f = open(file_name, 'w')
    f.write('\n'.join(lines) + '\n')

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

    input.extend([0, 0]) # Ensure that each string is a triple
    r_1 = [tuple(input[x:x+3]) for x in b_1]
    r_2 = [tuple(input[x:x+3]) for x in b_2]
    input = input[:-2]

    r = r_1 + r_2

    r_prime = radix.radix_sort(r, max(input))

    a_dict = rank(r, r_prime)
    b_dict = {}
    tmp = {}
    counter = 0
    for x in c:
        b_dict[x] = a_dict[counter]
        tmp[a_dict[counter]] = x
        counter += 1

    b12_sorted_index = []

    for i in xrange(1, counter + 1):
        b12_sorted_index.append(tmp[i])

    b_dict[len(input)] = 0
    b_dict[len(input) + 1] = 0

    b0_dict = {}
    b0_list = []
    max_ = 0
    for x in b_0:
        b0_dict[(input[x], b_dict[x + 1])] = x
        if input[x] > max_:
            max_ = input[x]
        if b_dict[x + 1] > max_:
            max_ = b_dict[x + 1]
        b0_list.append((input[x], b_dict[x + 1], 0))

    b0_sorted = radix.radix_sort(b0_list, max_)
    b0_sorted = [x[:-1] for x in b0_sorted]

    b0_sorted_index = [b0_dict[x] for x in b0_sorted]

    sorted_array = []
    i, j = 0, 0  # Positions in b0, b12
    while i < len(b0_sorted_index) and j < len(b12_sorted_index):
        if b12_sorted_index[j] % 3 == 1:
            if input[b0_sorted_index[i]] < input[b12_sorted_index[j]]:
                sorted_array.append(b0_sorted_index[i])
                i += 1
            elif input[b0_sorted_index[i]] > input[b12_sorted_index[j]]:
                sorted_array.append(b12_sorted_index[j])
                j += 1
            else:
                if b_dict[b0_sorted_index[i] + 1] < b_dict[b12_sorted_index[j] + 1]:
                    sorted_array.append(b0_sorted_index[i])
                    i += 1
                else:
                    sorted_array.append(b12_sorted_index[j])
                    j += 1
        elif b12_sorted_index[j] % 3 == 2:
            if input[b0_sorted_index[i]] < input[b12_sorted_index[j]]:
                sorted_array.append(b0_sorted_index[i])
                i += 1
            elif input[b0_sorted_index[i]] > input[b12_sorted_index[j]]:
                sorted_array.append(b12_sorted_index[j])
                j += 1
            else:
                if input[b0_sorted_index[i] + 1] < input[b12_sorted_index[j] + 1]:
                    sorted_array.append(b0_sorted_index[i])
                    i += 1
                elif input[b0_sorted_index[i] + 1] > input[b12_sorted_index[j] + 1]:
                    sorted_array.append(b12_sorted_index[j])
                    j += 1
                else:
                    if b_dict[b0_sorted_index[i] + 2] < b_dict[b12_sorted_index[j] + 2]:
                        sorted_array.append(b0_sorted_index[i])
                        i += 1
                    else:
                        sorted_array.append(b12_sorted_index[j])
                        j += 1

    while i < len(b0_sorted_index):
        sorted_array.append(b0_sorted_index[i])
        i += 1

    while j < len(b12_sorted_index):
        sorted_array.append(b12_sorted_index[j])
        j += 1

    return sorted_array

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

    for x in r:
        r_prime_rank.append(a_map[x])

    if len(a_set) != len(r):
        r_prime_rank.append(0)
        r_prime_suffix_array = dc3(r_prime_rank)[1:]
        a_dict = {r_prime_suffix_array[i]: (i + 1) for i in r_prime_suffix_array}

    else:
        a_dict = {i:r_prime_rank[i] for i in xrange(len(r_prime_rank))}
    
    return a_dict

def to_integer_alphabet(string):
    character_set = set(x for x in string)
    character_mapping = {}
    for char in LEXICALGRAPHICAL_ALPHABET:
        if char in character_set:
            character_mapping[char] = len(character_mapping)
    return [character_mapping[i] for i in string]

def bwt(input_str):
    int_alpha_str = to_integer_alphabet(input_str)
    sorted_array = dc3(int_alpha_str)

    result = ""
    result_1 = ""
    for i in sorted_array:
        result += input_str[i]
        result_1 += input_str[(i - 1) % len(input_str)]
    return result_1

def ibwt(last_col):
    char_count = dict()
    char_set = set()
    count = 0
    _b = dict()
    c = list()
    for char in last_col:
        if char in char_set:
            c += [char_count[char]]
            char_count[char] += 1
            _b[char] += [count]
        else:
            char_set.add(char)
            _b[char] = [count]
            c += [0]
            char_count[char] = 1
        count += 1
    first_col = "".join([(char_count[char] * char) for char in sorted(char_count.keys())])
    _a = dict()
    count = 0
    for char in sorted(char_count.keys()):
        _a[char] = count
        count += char_count[char]
    m = _a.copy()
    v = list()
    w = list()
    for char in last_col:
        v.append(_a[char])
        _a[char] += 1
    for char in first_col:
        w.append(_b[char][0])
        _b[char] = _b[char][1:]
    final_string = "$"
    j = 0
    final_string = first_col[v[j]] + final_string 
    j = v[j]
    while v[j] != 0:
        final_string = first_col[v[j]] + final_string
        j = v[j]
    return final_string

def main():
    parser = argparse.ArgumentParser(description='Burrows-Wheeler Transformation')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-bwt", action="store_true", help="performs the Burrows-Wheeler Transformation.")
    group.add_argument("-ibwt", action="store_true", help="performs the inverse Burrows-Wheeler Transformation.")
    parser.add_argument('input_file', type=str, help="the input FASTA file")
    parser.add_argument('output_file', type=str, help="the output FASTA file")

    args = parser.parse_args()

    input_str = read_file(args.input_file)[-1:][0]

    if args.bwt:
        output_str = bwt(input_str)
    else:
        output_str = ibwt(input_str)

    # ibwt("annb$aa")
    # ibwt("arbbr$aa")

    write_file(args.output_file, output_str)

if __name__ == "__main__":
    main()