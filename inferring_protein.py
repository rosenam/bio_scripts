"""
Austin Rosen

Inferring Protein From Spectrum -- Rosalind Problem
"""

def main():

    mass_dict = {}
    mass = []
    results = ''


    in_handle = open('prot.txt')
    table_handle = open('aa_mass.txt')

    with table_handle:
        for line in table_handle:
            chunks = line.split()
            mass_dict[round(float(chunks[1]),2)] = chunks[0]

    for line in in_handle:
        mass.append(line.strip())

    for i in range(1,len(mass)):
        tmp = round(float(mass[i])-float((mass[i-1])),2)
        ans = mass_dict.get(tmp)
        results += ans


    print(results)
if __name__ == "__main__":
    main()