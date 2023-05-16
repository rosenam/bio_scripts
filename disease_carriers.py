"""
Austin Rosen

Counting Disease Carriers -- Rosalind Exercise

"""

import math

def main():

    in_handle = open('carriers.txt')

    results = []

    for line in in_handle:
        line = line.strip()
        nums = line.split()

    for i in nums:
        q2 = float(i)
        tpq = 2*math.sqrt(q2)*(1-math.sqrt(q2))
        ans = round(q2 + tpq,3)
        results.append(ans)

    print(nums)
    print(*results)

if __name__ == "__main__":

    main()