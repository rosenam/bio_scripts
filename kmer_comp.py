"""
Austin Rosen

K-mer composition -- Rosalind problem
"""

def main():

    in_handle = open('kmer_comp.txt')
    seq = ''
    k = 4
    # read in sequence from file
    for line in in_handle:
        if line[0] != '>':
            seq += line.strip()

    # view sequence
    print(seq)
    print(len(seq))

    # save kmers from seq into list
    kmer_list = []
    for i in range(len(seq) - k + 1):
        tmp = seq[i:i + k]
        kmer_list.append(tmp)

    # view kmers
    print(len(kmer_list))
    print(kmer_list)


    # build alphabet and initialize variables
    alphabet = list('ACGT')
    k_mer = alphabet
    all_strings = []
    k = 3

    # build dictionary to store custom alphabet order
    custom_alph = {' ': 0}
    i = 1
    for e in alphabet:
        custom_alph[e] = i
        i += 1

    # loop through k values to make all possible strings of length k
    k = 3
    make_strings(all_strings, alphabet, k_mer, k)

    # find number of occurences of each kmer
    occur = ''
    for i in all_strings:
        n = 0
        for k in kmer_list:
            if i in k:
                n += 1
        occur += str(n) + ' '

    print(occur)


def make_strings(all_strings, alphabet, k_mer, k):
    # build all strings for each k value
    for l in range(k):
        k_mer = [i + j for i in alphabet for j in k_mer]

    # save strings into list
    for i in k_mer:
        all_strings.append(i)

    print(all_strings)
    print(len(all_strings))




if __name__ == '__main__':

    main()