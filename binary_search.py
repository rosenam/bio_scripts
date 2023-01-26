"""
Austin Rosen
Binary Search Algorithm
"""


##################################
def main(n, m, k, l):
    '''
    This function makes calls to the binary search algorithm,
    and writes the output to a file.
    '''

    out_handle = open("binary_search_results.txt", "w")
    for num in l:
        binary(k, num, out_handle)
    return


##################################

def binary(k, num, out_handle):
    """
    This function performs the binary search, with recursive calls to the function
    """

    min = 0
    max = len(k)-1
    mid = 0

    while min <= max:

        mid = (min + max) // 2

        if int(num) < int(k[mid]):
            max = mid - 1

        elif int(num) > int(k[mid]):
            min = mid + 1
        else:
            mid = mid + 1
            print(mid)
            out_handle.write(str(mid) + " ")
            return
    print("-1")
    out_handle.write("-1 ")
    return

####################################

if __name__ == "__main__":

    in_handle = open("rosalind_bins.txt")  # read in data

    with in_handle:  # turn data into proper format for the main() function
        data = [0, 0, 0, 0]
        i = 0
        for line in in_handle:
            data[i] = line.rstrip()
            i += 1
        n = data[0]
        m = data[1]
        k = data[2].split()
        l = data[3].split()

        main(n, m, k, l)

###########################################
