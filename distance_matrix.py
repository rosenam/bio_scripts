"""
Austin Rosen

Distance Matrix -- Rosalind Problem

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer
    is allowed an absolute error of 0.001.
"""

import pandas as pd
def main():

    # read in file
    in_handle = open('dist_mat.txt')

    # create a dictionary to store samples and their associated sequences
    my_dict = {}
    for line in in_handle:
        if line[0] == '>':
            name = line[1:].strip()
            my_dict[name] = ''
        else:
            my_dict[name] += line.rstrip()

    print(my_dict)

    # make algorithm for pairwise calculation of hamming distances
    seqs = list(my_dict.values())
    ratios = []
    df = pd.DataFrame()

    for seq in my_dict.values():
        ratios = []
        for other in seqs:
            n = 0
            for i in range(len(seq)):
                if seq[i] != other[i]:
                    n += 1

            r = n/len(seq)
            ratios.append(r)

        df_rat = pd.DataFrame(ratios)
        df = pd.concat([df, df_rat], axis=1)


    print(df.to_string(index=False, header=False))

if __name__ == '__main__':

    main()