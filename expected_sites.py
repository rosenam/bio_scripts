"""
Austin Rosen

Expected Number of Restriction Sites -- Rosalind Problem
"""

def main():

    n = 881007
    seq = 'CCTTGGTTGT'
    gc = [0.000, 0.122, 0.177, 0.206, 0.303, 0.351, 0.408, 0.490, 0.529, 0.612, 0.633, 0.732, 0.758, 0.863, 0.890, 1.000]
    results = []


    for e in gc:
        prob = 1
        for nt in seq:
            if nt == 'C' or nt == 'G':
                prob = prob * e / 2
            else:
                prob = prob * ((1 - e) / 2)
        ans = prob * (n-1)
        results.append(round(ans, 3))

    print(*results)

if __name__ == "__main__":

    main()