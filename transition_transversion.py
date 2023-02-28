"""
Austin Rosen
"""

def main():

    seq1 = []
    seq2 = []
    transitions = 0
    transversions = 0


    with open('trans_test.txt') as in_handle:
        i = 0
        for line in in_handle:
            if line[0] == '>':
                i+=1
            elif i == 1:
                seq1.append(line.strip())
            else:
                seq2.append(line.strip())

    seq1 = ''.join(seq1)
    seq2 = ''.join(seq2)

    print(seq1)
    print(seq2)

    i = 0
    for nt in seq1:
        if nt == seq2[i]:
            i += 1
        else:
            if (nt == 'A' or nt == 'G') and (seq2[i] == 'A' or seq2[i] == 'G'):
                transitions += 1
                i += 1
            elif (nt == 'C' or nt == 'T') and (seq2[i] == 'C' or seq2[i] == 'T'):
                transitions += 1
                i += 1
            elif (nt == 'A' or nt == 'C') and (seq2[i] == 'A' or seq2[i] == 'C'):
                transversions += 1
                i += 1
            elif (nt == 'G' or nt == 'T') and (seq2[i] == 'G' or seq2[i] == 'T'):
                transversions += 1
                i += 1
            elif (nt == 'C' or nt == 'G') and (seq2[i] == 'C' or seq2[i] == 'G'):
                transversions += 1
                i += 1
            elif (nt == 'A' or nt == 'T') and (seq2[i] == 'A' or seq2[i] == 'T'):
                transversions += 1
                i += 1

    ratio = round(transitions/transversions, 11)

    print(ratio)
if __name__ == '__main__':

    main()