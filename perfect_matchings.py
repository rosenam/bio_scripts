"""
Austin Rosen
"""
import math
def main():

    seq = 'CAAACCCCUUACCCCCGGGUAAAUGGAUUGUCGGGGCGCCACGGCCCAGGACCGAUAUUAGGGGUCUAGCCUUACGUGGU'
    a_count = seq.count('A')
    g_count = seq.count('G')

    num_matchings = math.factorial(a_count) * math.factorial(g_count)

    print(num_matchings)

if __name__ == '__main__':

    main()

