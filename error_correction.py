"""
Austin Rosen

Error Correction in Read -- Rosalind Problem

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated
    with a single-nucleotide error. For each read s in the dataset, one of the following applies:

 - s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
 - s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct
        read in the dataset (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution,
        and you may return the corrections in any order.)

"""

def main():

    in_handle = open('corr.txt')
    out_handle = open('corr_ans.txt', 'w')

    seq = []
    rc_seq = []
    correct = []
    incorrect = []
    # build list of sequences and their reverse complements
    with in_handle:
        for line in in_handle:
            if line[0] != '>':
                seq.append(line.strip())
                r_c = rev_comp(str(line))
                rc_seq.append(r_c.strip())

    full = seq + rc_seq

    # iterate over each sequence and its reverse complement to determine if the sequence is correct or incorrect
    for i in seq:

        seq_copy = seq.copy()
        seq_copy.remove(i)

        if i in seq_copy or rev_comp(i) in seq_copy:
            if i not in correct:
                correct.append(i)


    # iterate through correct sequences to make list of all incorrect sequences
    for i in seq:
        if i not in correct:
            incorrect.append(i)

    print(seq)
    print(correct)
    print(incorrect)
    print(len(seq))
    print(len(correct))
    print(len(incorrect))

    # find which correct sequence has a Hamming distance of 1 to each incorrect sequence
    for i in incorrect:
        for j in correct:
            if dist(i,j) == 1:
                # print(f'{i}-->{j}')
                out_handle.write(f'{i}->{j}\n')
                break

# find Hamming distance between strings i and j
def dist(i, j):

    d = 0
    for a,b in zip(i,j):
        if a != b: d+= 1

    return d

def rev_comp(line):

    translation_table = str.maketrans('ACGT', 'TGCA')
    r_c = line.translate(translation_table)[::-1]

    return r_c


if __name__ == '__main__':

    main()

