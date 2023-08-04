"""
Austin Rosen

Working with Files -- Rosalind Exercise
"""

def main():

    in_handle = open("file.txt")
    out_handle = open("out.txt", "w")
    count = 1

    with in_handle, out_handle:
        for line in in_handle:
            if count % 2 == 0:
                out_handle.write(line)
            count += 1

if __name__ == "__main__":

    main()