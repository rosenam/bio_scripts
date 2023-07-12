"""
Austin Rosen

Using the Spectrum Graph to Infer Peptides -- Rosalind Exercise
"""

def main():

    # read in data
    in_handle = open('spec_graph.txt')
    L = []
    for line in in_handle:
        L.append(float(line.strip()))

    # read in amino acid mass table
    mass_dict = {}
    table_handle = open('aa_mass.txt')
    with table_handle:
        for line in table_handle:
            chunks = line.split()
            mass_dict[chunks[0]] = round(float(chunks[1]), 4)

    # iterate through each as the starting point to find maximum increasing sequence
    longest = []
    length = 0
    for i in L:
        match = find_match(L, i, mass_dict)
        if len(match) > length:
            length = len(match)
            longest = match.copy()

    # find protein sequence associated with longest sequence
    prot = ''
    for k in longest:
        myKeys = list(mass_dict.keys())
        myVals = list(mass_dict.values())
        idx = myVals.index(k)
        AA = myKeys[idx]
        prot += AA

    # print protein sequence to user
    print(prot)
def find_match(L_tmp, i, mass_dict):

    # iterates through remaining values in L, and adds a difference if it is in the amino acid weight table
    results = []
    L_tmp.remove(i)
    final = []
    for j in L_tmp:
        ans = j - i
        ans = round(ans,4)
        if ans in mass_dict.values():
            results.append(ans)
            i = j

    return results

if __name__ == "__main__":

    main()