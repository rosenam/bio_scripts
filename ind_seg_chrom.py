"""
Austin Rosen

Independent Segregation of Chromosomes -- Rosalind Problem

"""

import math
def main():

    n = 40
    values = []
    results = []
    final = []
    for i in range(2*n,0,-1):
        values.append((math.factorial(2*n)/math.factorial(i)/math.factorial(2*n-i))*0.5**(2*n))
        results.append(round(math.log(sum(values),10),3))
    results.reverse()

    print(*results)


if __name__ == "__main__":

    main()