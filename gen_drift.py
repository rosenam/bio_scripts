"""
Austin Rosen

The Wright-Fisher Model of Genetic Drift -- Rosalind Exercise

"""

import math
def main():

    n = 4
    m = 6
    g = 2
    k = 1

    p = m/(2*n)

    q2 = (1-p)**2
    tpq = 2 * math.sqrt(q2) * (1 - math.sqrt(q2))
    ans = round(q2 + tpq, 3)


    prob = (math.factorial(2*n)/math.factorial(k)/math.factorial(2*n-k))*(p**k)*(1-p)**(2*n-k)

    print(ans)
    print(prob)

if __name__ == "__main__":

    main()