"""
Austin Rosen

Speeding Up Motif Finding -- Rosalind Problem
"""

def main():

    # initialize variables
    seq = ''
    n = 0
    out_handle = open('motif_speed_results.txt', 'w')
    in_handle = open('motif_speed.txt')

    # read in sequence data
    in_handle = open('motif_speed.txt')
    for line in in_handle:
        if line[0] != '>':
            seq += line.strip()


    # build failure array
    out_handle.write('0')
    for i in range(1,len(seq)):
        if seq[n] == seq[i]:
            n += 1
        else:
            while n > 0 and seq[0:n] != seq[i-n+1:i+1]:
                    n -= 1
        out_handle.write(f' {str(n)}')


if __name__ == "__main__":

    main()