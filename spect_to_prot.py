"""
Austin Rosen

Comparing a Spectrum to a Protein -- Rosalind Problem
"""

def main():

    # read in data
    in_handle = open('spect_to_prot.txt')

    l = 0
    prots = []
    R_set = []
    ANS = {}

    for line in in_handle:
        if l == 0:
            n = int(line)
            l += 1
        elif l <= n:
            prots.append(line.strip())
            l += 1
        else:
            R_set.append(float(line))

    # read in amino acid mass table
    mass_dict = {}
    table_handle = open('aa_mass.txt')
    with table_handle:
        for line in table_handle:
            chunks = line.split()
            mass_dict[chunks[0]] = round(float(chunks[1]), 6)

    # iterate through each protein
    for prot in prots:

        results = []
        final = {}

        # build the complete spectrum (all prefix and suffixes) for each given string
        S_set = build_multiset(prot, mass_dict)

        # find the weights of each prefix/suffix
        S_weight = find_weight(S_set, mass_dict)

        # find differences between R and S
        for x in R_set:
            for y in S_weight.values():
                ans = round(abs(x-y), 4)
                if ans in results:
                    final[ans] += 1
                else:
                    final[ans] = 1
                results.append(ans)

        # find max multiplicity and put answer in a dictionary
        M = max(final.values())
        ANS[prot] = M

    print(max(ANS.values()))
    print(ANS)

def build_multiset(S, mass_dict):
    S_set = {}
    for i in range(len(S)-1):
        prefix = S[0:i+1]
        suffix = S[-1:i:-1]
        S_set[prefix] = find_weight(prefix, mass_dict)
        S_set[suffix] = find_weight(suffix, mass_dict)
    return S_set

def find_weight(S_set, mass_dict):
    S_weight = {}
    for s in S_set:
        tmp = 0
        for aa in s:
            tmp += mass_dict.get(aa)
        S_weight[s] = tmp
    return S_weight
if __name__ == "__main__":

    main()