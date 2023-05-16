"""
Austin Rosen

Shortest Superstring -- Rosalind Problem
"""


def main():

    # open input file
    in_handle = open('superstring.txt')

    # initialize variables
    seq = []
    tmp = ''


    # store sequences in a list
    for line in in_handle:
        if line[0] != '>':
            tmp += line.strip()
        else:
            seq.append(tmp)
            tmp = ''
    seq.pop(0)
    seq.append(tmp)


    ### build superstring from sequences
    super_string = str(seq.pop(0))

    # loop through substrings to build larger and larger superstring until all substrings have been used
    while len(seq) > 0:
        for tmp in seq:
            for a in range(len(tmp) - 1, int(len(tmp)/2), -1):
                slice_front, slice_rear = tmp[0:a], tmp[-a:]
                if slice_front in super_string[-a:]:
                    add = str(*tmp.split(slice_front)[-1:])
                    super_string += add
                    seq.remove(tmp)
                    break
                elif slice_rear in super_string[0:a]:
                    add = tmp.split(slice_rear)[0]
                    super_string = add + super_string
                    seq.remove(tmp)
                    break

    # print result to user
    print(super_string)

if __name__ == '__main__':

    main()