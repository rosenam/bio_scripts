"""
Austin Rosen

"""

import math

def main():

    n = 5
    nums = []
    total = 1
    for i in range(1,n+1):
        total = total * i
        nums.append(i)

    print(total)

    permute(nums, 0, n)


def permute(nums, x, n):

    if x == n:
        out = ''
        for e in nums:
            out += str(e) + ' '

        print(out)

    else:
        for i in range(x,n):
            nums[x], nums[i] = nums[i], nums[x]
            permute(nums, x+1 ,n)
            nums[x], nums[i] = nums[i], nums[x]


if __name__ == '__main__':

    main()

