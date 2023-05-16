"""
Austin Rosen

Introduction to Alternative Splicing -- Rosalind Problem

Given: Positive integers n and m with 0≤m≤n≤2000

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk)

C(n,k) = n! / [ (n-k)! k! ]
"""

import math
def main():

    n = 1621
    m = 1092

    sum = 0
    for k in range(m,n+1):
        C = (math.factorial(n)//(math.factorial(n-k)*math.factorial(k)))
        sum += C
    sum = sum % 1000000
    print(sum)
if __name__ == '__main__':

    main()