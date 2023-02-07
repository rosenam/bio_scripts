"""
Austin Rosen

Rosalind ...
"""

def main():

    # open the requisite files
    table_handle = open('aa_table.txt')
    in_handle = open('mrna.txt')

    # initialize dictionary object for amino acid table
    aa_dict = {}

    # build amino acid dictionary from Rosalind table
    with table_handle:
        for line in table_handle:
            chunks = line.split()

            aa_dict[chunks[0]] = chunks[1]
            aa_dict[chunks[2]] = chunks[3]
            aa_dict[chunks[4]] = chunks[5]
            aa_dict[chunks[6]] = chunks[7]

    aa = ''
    product = 3
    for line in in_handle:
        aa = aa + line.rstrip()


    for e in aa:
        count = 0
        for val in aa_dict.values():
            if val == e:
                count += 1
        product = (product * count) % 1000000

    print(product)

if __name__ == '__main__':

    main()