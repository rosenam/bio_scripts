"""
Austin Rosen

Inferring Peptide from Full Spectrum -- Rosalind Exercise
"""

def main():


    l = 0
    nums = []
    diff = []
    mass_dict = {}
    in_handle = open('full_spec.txt')
    table_handle = open('aa_mass.txt')
    results = []
    k = 0
    pep = ''

    with table_handle:
        for line in table_handle:
            chunks = line.split()
            mass_dict[round(float(chunks[1]), 5)] = chunks[0]

    for line in in_handle:
        if l == 0:
            full_mass = round(float(line),5)
        else:
            nums.append(round(float(line),5))
        l += 1

    n = int(((l-3)/2))
    print(n)
    print(nums)
    print(mass_dict)


    for i in nums:
        tmp = nums.copy()
        tmp.remove(i)
        print(tmp)
        for j in tmp:
            x = round(abs(i-j),5)
            if x in mass_dict.keys():
                results.append(x)
                break

    print(results)

    final = results[:n]

    v_lst = list(mass_dict.values())
    k_lst = list(mass_dict.keys())
    for i in final:
        idx = k_lst.index(i)
        prt = v_lst[idx]
        pep += prt

    print(pep)

if __name__ == "__main__":

    main()