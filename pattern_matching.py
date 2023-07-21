"""
Austin Rosen

Introduction to Pattern Matching -- Rosalind Exercise
"""

def main():

    # read sequences
    seqs = []
    with open('patterns.txt') as in_handle:
        for line in in_handle:
            seqs.append(line.strip())

    # initialize dict and child node number
    node_dict = {}
    child = 2

    # iterate through seqs to build a dictionary with a parent node, and each
    # of it's child nodes and the letter associated with each of the resulting edges
    for seq in seqs:
        parent = 1
        for char in seq:
            if parent in node_dict.keys():
                if char in node_dict[parent].values():
                    v_list = list(node_dict[parent].values())
                    k_list = list(node_dict[parent].keys())
                    idx = v_list.index(char)
                    parent = k_list[idx]
                else:
                    node_dict[parent].update({child:char})
                    parent = child
                    child += 1
            else:
                node_dict[parent] = {child:char}
                child += 1
                parent += 1

    # write the results to a file in the correct format
    out_handle = open('trie.txt', 'w')
    for x,y in node_dict.items():
        ans = str(x) + ' '
        for key in y:
            tmp = ans
            tmp = tmp + str(key) + ' '
            tmp = tmp + node_dict[x][key] + '\n'
            print(tmp)
            out_handle.write(tmp)

if __name__ == "__main__":

    main()