"""
Austin Rosen

Longest Increasing Subsequence - Rosalind Project
"""

def main():

    n = 5
    order = '5 1 4 2 3'
    order = order.split(' ')
    print(order)
    dup = order.copy()
    ascend = []

    for i in order:
        tmp = [i]
        dup.remove(i)
        print(dup)
        for j in dup:
            if int(j) > int(tmp[-1]):
                print(int(j))
                print(int(tmp[-1]))
                tmp.append(j)

        if len(tmp) > len(ascend):
            ascend = tmp

    print(ascend)


if __name__ == '__main__':

    main()