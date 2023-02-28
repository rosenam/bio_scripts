"""
Austin Rosen

"""
import math
def main():

    seq = 'AGGGGTCGTCACAGTTCTGAGGAAGCAAGACGGGATCGAGCTTTTGATGACTATACACCAGCGGTTCCGCTGCACGACCTGAACGACAATCTTGTT'
    probs = '0.078 0.128 0.209 0.246 0.335 0.371 0.456 0.482 0.530 0.603 0.664 0.708 0.777 0.838 0.936'
    probs = probs.split(' ')

    print(seq, probs)
    final = ''

    for e in probs:
        total = 0
        for nt in seq:
            if nt == 'G' or nt == 'C':
                total = total + math.log10(float(e)/2)
            else:
                total = total + math.log10((1 - float(e))/2)

        total = round(total, 3)
        final += str(total) + ' '

    print(final)

if __name__ == '__main__':

    main()