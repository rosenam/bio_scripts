"""
Austin Rosen

Constructing a De Bruijn graph  -- Rosalind Exercise
"""

def main():

    # read in data
    in_handle = open('debruijn.txt')
    seqs = []
    all_seqs = []
    for line in in_handle:
        seqs.append(line.strip())

    # find reverse complement of each sequence and store forward and rev comp of sequences in a new list
    for seq in seqs:
        all_seqs.append(seq)
        all_seqs.append(rev_comp(seq))

    # find just unique seqs
    all_seqs = list(set(all_seqs))

    # build DB graph adjacency list
    results = []
    out_handle = open('db_ans.txt', 'w')

    for seq in all_seqs:
        ans = '(' + seq[0:len(seq) - 1] + ', ' + seq[1:len(seq)] + ')' + '\n'
        results.append(ans)
        print(ans)
        out_handle.write(ans)

def rev_comp(seq):

    t_table = str.maketrans('ACGT', 'TGCA')
    comp = seq.translate(t_table)

    rev_comp = comp [::-1]

    return rev_comp


if __name__ == "__main__":

    main()