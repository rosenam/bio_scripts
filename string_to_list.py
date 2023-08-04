"""
Austin Rosen

Strings and Lists -- Rosalind Exercise
"""

def main():

    with open('string_list.txt') as in_handle:

        text, idx  = in_handle.readline(), in_handle.readline().split()
        print(text[int(idx[0]):int(idx[1])+1], text[int(idx[2]):int(idx[3])+1], sep = " ")

if __name__ == "__main__":

    main()

