"""
Austin Rosen
"""

def main():

    seq = []
    motif = []

    with open('motif_test.txt') as in_handle:
        i = 0
        for line in in_handle:
            if line[0] == '>':
                i+=1
            elif i == 1:
                seq.append(line.strip())
            else:
                motif.append(line.strip())

    seq = ''.join(seq)
    tmp_seq = seq
    motif = ''.join(motif)


    idx = []
    i = 0
    for nt in motif:
        i = tmp_seq.index(nt) + i + 1
        idx.append(i)
        tmp_seq = seq[i:]
        print(i)
        print(tmp_seq)


    print(*idx)




if __name__ =='__main__':

    main()