"""
Austin Rosen
"""

#####################################
def main():

    # open the requisite files
    table_handle = open('aa_table.txt')
    in_handle = open('rosalind_splc.txt')

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

    # initialize variables

    intron = []
    cdn = []
    acids = ''
    seq = ''

    i = 0
    for line in in_handle:
        if line[0] == '>':
            i += 1
        elif i == 1:
            seq += line.strip()
        else:
            intron.append(line.strip())

    print(seq)
    print(intron)
    for i in intron:
        temp = seq.strip().split(i)
        seq = ''.join(temp)

    translation_table = str.maketrans('T', 'U')
    rna = seq.translate(translation_table)

    size = int(len(rna) / 3)

    for i in range(0, size):
        cdn.insert(i, rna[:3])
        rna = rna[3:]

    print(cdn)
    print(aa_dict)
    # compare each codon to the amino acid dictionary
    for key in cdn:
        if aa_dict[key] != 'Stop':
            acids += aa_dict[key]

    # print the amino acid sequence
    print(acids)

    return


#####################################
if __name__ == '__main__':

    main()
######################################