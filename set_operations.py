"""
Austin Rosen

Introduction to Set Operations -- Rosalind Problem
"""

def main():

    # open input and output files
    in_handle = open('sets.txt')
    out_handle = open('set_results.txt', 'w')

    # initialize variables
    n = 0
    l = 0
    a = ''
    b = ''

    # read in input data
    for line in in_handle:
        if l == 0:
            n = int(line)
            l += 1
        elif line[0] == '{' and l == 1:
            a += line[1:].strip()
            l += 1
        elif l == 2 and '}' not in line:
            a += line.strip()
        elif l == 2 and '}' in line:
            a += line[0:-2].strip()
            l += 1
        elif line[0] == '{' and l == 3:
            b += line[1:].strip()
            l += 1
        elif l == 4 and '}' not in line:
            b += line.strip()
        elif l == 4 and '}' in line:
            b += line[0:-2].strip()

    # get data into correct format
    a = a.replace(' ','').split(',')
    b = b.replace(' ','').split(',')
    A = []
    B = []

    # turn data into list of integers
    for i in a:
        A.append(int(i))
    for i in b:
        B.append(int(i))

    # call functions to perform different set methods
    add(A, B, out_handle)
    and_fx(A, B, out_handle)
    subtract(A, B, out_handle)
    subtract(B, A, out_handle)
    comp(A, n, out_handle)
    comp(B, n, out_handle)

# finds OR of two sets
def add(A, B, out_handle):

    result = list(A)
    for i in B:
        if i not in A:
            result.append(i)

    print(f'{{{", ".join(map(str, result))}}}')
    out_handle.write(f'{{{", ".join(map(str, result))}}}')

# subtracts set B from set A
def subtract(A, B, out_handle):

    result = list(A)
    for i in B:
        if i in A:
            result.remove(i)

    print(f'{{{", ".join(map(str, result))}}}')
    out_handle.write(f'{{{", ".join(map(str, result))}}}')

# takes intersection of sets A and B
def and_fx(A, B, out_handle):

    result = []
    for i in B:
        if i in A:
            result.append(i)

    print(f'{{{", ".join(map(str, result))}}}')
    out_handle.write(f'{{{", ".join(map(str, result))}}}')

# takes the complement of A in comparison to N
def comp(A, n, out_handle):

    result = []
    for i in range(1,n+1):
        result.append(i)

    for i in A:
        if i in result:
            result.remove(i)

    print(f'{{{", ".join(map(str, result))}}}')
    out_handle.write(print(f'{{{", ".join(map(str, result))}}}'))


if __name__ == '__main__':

    main()