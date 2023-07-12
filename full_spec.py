"""
Austin Rosen

Inferring Peptide from Full Spectrum -- Rosalind Exercise
"""

def main():


    l = 0
    nums = []
    mass_dict = {}
    in_handle = open('full_spec.txt')
    table_handle = open('aa_mass.txt')
    results = []

    # read in amino acid mass table
    with table_handle:
        for line in table_handle:
            chunks = line.split()
            mass_dict[round(float(chunks[1]), 4)] = chunks[0]

    # read in mass data from partial digest
    for line in in_handle:
        if l == 0:
            full_mass = round(float(line),5)
        else:
            nums.append(round(float(line),5))
        l += 1

    ### find inner t string from given data

    # initialize variables
    n = int(((l-3)/2))
    tmp = nums[0]

    # iterate through loop n times to find n amino acids
    for i in range(1,n+1):
        nums.remove(tmp)
        for j in nums:
            mass = round(j - tmp, 4)
            if mass in mass_dict.keys():
                aa = mass_dict.get(mass)
                results.append(aa)
                tmp = j
                break
        i += 1

    # print results to user

    final = ''
    for i in results:
        final += i

    print(final)

if __name__ == "__main__":

    main()