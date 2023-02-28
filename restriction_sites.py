"""
Austin Rosen

Location Restriction Sites -- Rosalind Problem
"""

def main():

    seq = 'CGCGTGTTCGAATTGTTTATTGTAGCACACCCACACCTCAGGGGAAATCGCGAATTGTTC' \
          'TCTAGTGTCTGCAGAATCAGGCTCTCGGCCCTTATAACCCCCATGGTCCATCCCACCTTA' \
          'ACCCAGACATGCAGGGCCGTCTCTCGACTGGAACGTTCCGTGAGCTGACCACGATGAGCC' \
          'AACCCACGTGACGGGCTTCCCCCCCTCCCCGTCGAGTAATCAAATCCCCATTTGTGGCGC' \
          'GTCTATCGGCCCCCACCAAGCGATGCTTCCTTTTGCGATTCAATATTCCAAACCGAAGTC' \
          'CAAGCACTTCGTTACTGTGCCAACAGTACAGGGCGTAAAGTGGATATGATTCATATACTG' \
          'CACTATAGTCGCGATGCTGGCAAAGTGTCAGACGGCTTTACGCATCATAGGCTTCACGAG' \
          'TTATGTTTAAAGGAGCAGTGTTCCAGACAGAGTCCCTCGCGTGCCTTTAAAGGCCGGGAC' \
          'CACTTGCTGTATGGGTGAACGGTAGTGGCAACATAAGCAGGCCTCGAGGGTGAGCTGCGG' \
          'GCAGAGCTCCTAATAGAGTGAGGGGTTGCTTGCCCATGGTTGGGGTCTAGAATGTCCATT' \
          'AACCGTAAGACATTCGCGATCGAGTCCCTCAGGGGGGCCCTTTGTAGGAGCCATTTTCGC' \
          'CGGTGCAAGACAACCTTGTGAGCGCCAATGGTCCTGATCTCCCGTCACATGGGATATCCC' \
          'TCATCGAGTTAGGAATTCGCCACGATATCCGTTCGGGTCTTAGGGTCTTTGTGACCGTAC' \
          'CGTAGTAAGTCCCGGGTTCCGTTTCGGCACTCGTGTGACAGTGTGTGTGGAGCGCGCATA' \
          'GAGTGGGCCTAGCGAAAGAATTGCACAAATTAACCTTGATTCAGTCGTTCAGGCAAACTG' \
          'TGATTGCCGAAGCAACGTCTTCTCTCCGGGACTATA'


    size = len(seq)
    trans_table = str.maketrans('ACGT', 'TGCA')
    results = dict()
    lst = []

    for i in range(0,size - 3):
        for k in range(4,13):
            if i + k > size:
                continue
            else:
                tmp = seq[i:i + k]
                comp = tmp.translate(trans_table)
                rev_comp = comp[::-1]
                if tmp == rev_comp:
                    print(i+1, k)
    # for k in range(4,13):
    #     for i in range(0,size - k + 1):
    #         tmp = seq[i:i+k]
    #         comp = tmp.translate(trans_table)
    #         rev_comp = comp[::-1]
    #         if tmp == rev_comp:
    #             idx = i +1
    #             if idx in results.keys():
    #                 print('in')
    #                 results[idx] = k
    #             else:
    #                 results[idx] = k
    #
    # myKeys = list(results.keys())
    # myKeys.sort()
    # sorted_dict = {i: results[i] for i in myKeys}
    #
    # total = 0
    # for k , v in sorted_dict.items():
    #     total += 1
    #     print(k,v)
    #
    #
    # print(total)
    #
    # print(lst)

if __name__ == '__main__':

    main()