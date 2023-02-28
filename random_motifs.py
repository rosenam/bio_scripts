"""
Austin Rosen
"""

def main():

    rdm_strings = 90000
    gc_cont = 0.6
    motif = 'ATAGCCGA'
    prob = 1


    for nt in motif:
        if nt == 'A' or nt == 'T':
            prob = prob*(1-gc_cont/2)
        elif nt == 'C' or nt == 'G':
            prob = prob*gc_cont/2



if __name__ == '__main__':

    main()