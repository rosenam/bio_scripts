"""
Austin Rosen
"""

import math
def main():

    # build alphabet and initialize variables
    alphabet = list('BVAQJXUYPFZ')
    k_mer = alphabet
    all_strings = []
    k = 3

    # build dictionary to store custom alphabet order
    custom_alph = {' ':0}
    i = 1
    for e in alphabet:
        custom_alph[e] = i
        i += 1

    # loop through k values to make all possible strings of length 1 to k
    for i in range(k):
        make_strings(all_strings, alphabet, k_mer, i)

    # sort all strings by lexicographic order given above
    sort_strings(all_strings, custom_alph)

def make_strings(all_strings, alphabet, k_mer, k):

    # build all strings for each k value
    for l in range(k):
        k_mer = [i + j for i in alphabet for j in k_mer]

    # save strings into list
    for i in k_mer:
        all_strings.append(i)

def sort_strings(all_strings, custom_alph):

    sorted_strings = list(all_strings.copy())

    out_handle = open('lexico_vary.txt', 'w')

    final_sort = sorted(sorted_strings, key=lambda word: [custom_alph.get(c, ord(c)) for c in word])

    for word in final_sort:
        out_handle.write(f'{word.strip()}\n')

if __name__ == '__main__':

    main()