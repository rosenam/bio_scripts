"""
Austin Rosen
"""

import math

def main():

    input = '95 9'
    input = input.split(' ')
    n , k = int(input[0]) , int(input[1])

    pperm = (math.factorial(n)/math.factorial(n-k)) % 1000000
    print(pperm)


if __name__ == '__main__':

    main()