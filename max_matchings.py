"""
Austin Rosen

Maximum Matchings and RNA Secondary Structures -- Rosalind Problem
"""

import math

def main():

    seq = 'AGAGCUAAUGACCCCUGCGUCUGAGCAUGAAUAUAGGUAGACUACGAGGAGGGUGGAACCAUUGUGCCUUACGCUCACCGUGACAAUGCGGUC'


    A_nt = seq.count('A')
    U_nt = seq.count('U')
    C_nt = seq.count('C')
    G_nt = seq.count('G')

    print(A_nt)
    print(U_nt)
    print(C_nt)
    print(G_nt)

    if A_nt > U_nt: tmp = math.factorial(A_nt)/math.factorial(A_nt-U_nt)
    else: tmp = math.factorial(U_nt)/math.factorial(U_nt-A_nt)

    if C_nt > G_nt: tmp_1 = math.factorial(C_nt)/math.factorial(C_nt-G_nt)
    else: tmp_1 = math.factorial(G_nt)/math.factorial(G_nt-C_nt)

    matchings = int(tmp*tmp_1)

    print(matchings)

if __name__ == '__main__':

    main()