"""
Austin Rosen

Genome Assembly with Perfect Coverage -- Rosalind Exercise

"""

def main():

    # read in data
    in_handle = open('assembly.txt')
    seqs = []
    for line in in_handle:
        seqs.append(line.strip())
    results = str(seqs[0])

    # use first seq as starting point of sequence, and build on that using all other sequences
    tmp = seqs.copy()
    tmp.pop(0)

    # iterate through each sequence to figure out which one to append to currently growing assembly
    # stop once string is of maximum length assuming full coverage
    for seq in seqs:
        for t in tmp:
            if results[len(results) - len(seq) + 1 :] == t[0:len(seq)-1]:
                results += t[-1]
                if len(results) == len(seqs):
                    print(results)
                    return


if __name__ == "__main__":

    main()