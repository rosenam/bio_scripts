"""
Austin Rosen

Comparing Spectra with the Spectral Convolution -- Rosalind Exercise
"""

def main():

    # open files and initialize variables
    in_handle = open('spectra.txt')
    spectra = []
    results = []
    final = {}
    n = 0

    # read in data
    with in_handle:
        for line in in_handle:
            spectra.append(line.split())

    # make a list for each spectra
    spec_1 = spectra[0]
    spec_2 = spectra[1]

    # substract one sprecta from the other and record values in a dictionary
    for i in spec_1:
        for j in spec_2:
            ans = round(float(i) - float(j),5)
            if ans in results:
                final[ans] += 1
            else:
                final[ans] = 1
            results.append(ans)


    # find maximum dictionary value, and print key and value
    M = max(final.values())
    print(M)
    k_lst = list(final.keys())
    v_lst = list(final.values())
    idx = v_lst.index(M)
    print(k_lst[idx])

if __name__ == "__main__":

    main()