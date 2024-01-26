"""
Austin Rosen

The Wright-Fisher Model of Genetic Drift -- Rosalind Exercise

v2: Here are some changes
"""

import math
def main():

    n = 4
    m = 6
    g = 2
    k = 1

    p = m/(2*n)
    ans = 1

    for i in range(2*n, 2*n-k-1, -1):

        ans -= p**i
        ans = round(ans, 3)


    prob = (math.factorial(2*n)/math.factorial(k)/math.factorial(2*n-k))*(p**k)*(1-p)**(2*n-k)

    print(ans)
    print(prob)

if __name__ == "__main__":

    main()