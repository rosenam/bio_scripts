"""
Austin Rosen

Degree Array -- Rosalind Exercise
"""

def main():

    in_handle = open("array.txt")
    my_dict = {}
    out_handle = open('out.txt','w')


    with in_handle:
        for line in in_handle:
            for num in line.split():
                if num in my_dict.keys():
                    my_dict[num] += 1
                else:
                    my_dict[num] = 1
    my_dict = dict(sorted(my_dict.items()))
    for key,value in my_dict.items():
        print(key,value)
        out_handle.write(str(value) + ' ')


if __name__ == "__main__":

    main()