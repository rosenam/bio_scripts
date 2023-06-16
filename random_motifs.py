"""
Austin Rosen

Matching Random Motifs - Rosalind
"""

def main():

    rdm_strings = 80160
    gc = 0.419381
    motif = 'CACTGATAG'
    prob = 1


    for nt in motif:
        if nt == 'C' or nt == 'G':
            prob = prob*gc/2
        else:
            prob = prob*((1-gc)/2)

    f_prob = 1 - prob

    print(1 - (f_prob ** rdm_strings))

if __name__ == '__main__':

    main()