"""
Austin Rosen

Rosalind Protein Mass
"""

def main():

    temp_dict = {}


    table_handle = open('aa_temps.txt')
    in_handle = open('rosalind_prmt.txt')

    # initialize dictionary object for amino acid mass table
    temp_dict = {}

    # build amino acid temp dictionary from Rosalind table
    with table_handle:
        for line in table_handle:
            chunks = line.split()
            temp_dict[chunks[0]] = chunks[1]

    # sum the temps of the aa's in the sequence and print result
    sum = 0
    with in_handle:
        for line in in_handle:
            for aa in line:
                sum += float(temp_dict[aa])
    print(round(sum, 3))

if __name__ == '__main__':

    main()