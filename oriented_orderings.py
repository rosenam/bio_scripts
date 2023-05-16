"""
Austin Rosen

"""

import math

def main():

    # 2 ^ n arrangements of negatives * n!
    n=3
    nums = []
    total = 1

    # make list of numbers
    for i in range(1,n+1):
        total = total * i
        nums.append(i)
        nums.append(-i)

    final = []

    # permute numbers
    permute(nums, 0, 2*n, final)


    out_handle = open('oriented.txt', 'w')

    # write results to file
    total = (2**n)*math.factorial(n)
    out_handle.write(f'{total}\n')
    for i in final:
        print(i)
        tmp = ' '.join(str(e) for e in i)
        out_handle.write(f'{tmp}\n')


def permute(nums, x, n, final):

    if x == n:
        # save only the first n numbers, make sure not a duplicate,
        # and make sure no two numbers have the same absolute value
        tmp = nums[0:int(n/2)]
        new = True
        for i in tmp:
            if -i in tmp:
                new = False
        if new == True:
            if nums[0:int(n/2)] not in final:
                final.append(nums[0:int(n/2)])

    else:
        for i in range(x, n):
            nums[x], nums[i] = nums[i], nums[x]
            permute(nums, x+1, n, final)
            nums[x], nums[i] = nums[i], nums[x]


if __name__ == '__main__':

    main()

