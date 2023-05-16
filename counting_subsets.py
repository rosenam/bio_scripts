"""
Austin Rosen

Counting Subsets - Rosalind Problem

Given: A positive integer n (n≤1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.

If n = 3, ans = 8
"""

def main():

    n = 932
    ans = (2**n)%1000000

    print(ans)

if __name__ == '__main__':

    main()