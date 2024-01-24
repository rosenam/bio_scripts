"""
Austin Rosen

Majority Element -- Rosalind Exercise
"""

def main():

    in_handle = open("in.txt")
    out_handle = open("out.txt", "w")
    arrays = []

    for line in in_handle:
        arrays.append(line.split())

    for array in arrays:
        ans = max(array,key=array.count)
        if int(ans) >= len(array)/2 + 1:
            out_handle.write(ans + ' ')
        else:
            out_handle.write("-1" + ' ')


if __name__ == "__main__":

    main()