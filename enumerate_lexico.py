"""
Austin Rosen
"""

def main():

    alph = 'ABCDEFGHIJ'
    alph = list(alph)
    my_dict = {}
    num = 3
    i = 1

    for e in alph:
        my_dict[i] = e
        i += 1


    for e in my_dict:
        letters = str(my_dict[e])
        tmp = my_dict.copy()
        for i in my_dict:
            letters = str(my_dict[e])
            for a in range(num-1):
                small = min(tmp, key=tmp.get)
                letters += str(tmp[small])

                del tmp[small]
            print(letters)


if __name__ == '__main__':

    main()