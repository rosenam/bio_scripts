"""
Austin Rosen

Distances in Trees -- Rosalind Problem
"""

def main():

    in_handle = open("trees.txt")
    i = 1
    taxa = []
    tree = ''

    for line in in_handle:
        if i % 3 == 1:
            newick = line
            i += 1
        elif i % 3 == 2:
            taxa1, taxa2 = line.split()[0], line.split()[1]
            taxa.append(taxa1)
            taxa.append(taxa2)
            i += 1

            btwn = ExtractString(taxa,newick)
            dist = FindDistance(btwn)

            print(btwn)
            print(dist)

        else:
            i += 1
            groups = []
            taxa = []

def ExtractString(taxa, newick):

    ### Find the string between the two taxa

    tmp = ''

    idx1 = newick.index(taxa[0])
    idx2 = newick.index(taxa[1])

    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
        taxa[0], taxa[1] = taxa[1], taxa[0]

    for idx in range(idx1 + len(taxa[0]), idx2):
        tmp = tmp + newick[idx]

    return tmp

def FindDistance(btwn):

    ### Takes the string between two taxa, and finds their distance

    p_sum = 0
    c_count = 0
    ratio = 0
    add_dist = 0
    print(btwn)

    for i in btwn:
        if i == '(':
            p_sum += 1
            ratio -= 1
            if c_count < 2:
                add_dist -= 1
            c_count = 0
        elif i == ')':
            p_sum += 1
            ratio += 1
            if c_count < 2:
                add_dist -= 1
            c_count = 0
        elif i == ',':
            c_count += 1

    if ratio == 0:
        dist = 2


    if abs(ratio) >= 1:
        if btwn[len(btwn) - 3] == '),':
            dist = 1 + p_sum
        else:
            dist = 2 + p_sum

    return dist + add_dist


if __name__ == "__main__":

    main()