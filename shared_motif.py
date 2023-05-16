"""
Austin Rosen

Finding a Shared Spliced Motif -- Rosalind Problem
"""

def main():

    in_handle = open('shared_motif.txt')

    seqs = []

    for line in in_handle:
        if line[0] != '>':
            seqs.append(line.strip())

    seq1 = str(seqs[0])
    seq2 = str(seqs[1])

    print(seqs)
    print(seq1)
    print(seq2)

    for nt in seq1:
        motif_search(nt, seq1, seq2)

motif_search(nt,seq1,seq2):

    for i in seq2:
        if i == nt

if __name__ == "__main__":

    main()