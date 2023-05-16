"""
Austin Rosen

Notes:

Need to find how many graph chunks there are, and the min number of edges
is the number of edges needed to connect them all together (num_chunks + nodes with no edges - 1)
"""



def main():

    # initialize variables
    in_handle = open('rosalind_tree.txt')
    l = 1
    adj = []
    tally = []
    line_lst = []
    missing = []
    final = []
    i = 0


    # read input file
    for line in in_handle:
        if l == 1:
            nodes = int(line)
        else:
            line = line.strip()
            line_lst = line.split()
            for j in line_lst:
                tally.append(j)
            adj.append(line.split())
        l += 1

    # make list of nodes
    nums = list(range(1, nodes+1))

    # find all nodes with no edges
    for i in range(1,nodes+1):
        if str(i) not in tally:
            missing.append(i)

    # iterate through adjacency list to find groupings of edges
    while len(adj) > 0:
        groups = []
        current = adj.pop(0)
        groups.append(current)
        find_group(current, adj, groups)
        i += 1
        final.append(list(groups))

    # view groupings
    #out_handle = open('tree_results.txt', 'w')
    for f in final:
        print(f)
        #out_handle.write(f'{str(f)}\n')


    # find min number of edges needed to complete the graph
    ans = len(final) + len(missing) - 1
    print(f'Number of Groups: {len(final)}')
    print(f'Number of Nodes with No Edges: {len(missing)}')
    print(f'Min # of Edges to Complete: {ans}')

# find groupings
def find_group(current, adj, groups):
    for x in current:
        for e in adj:
            if x in e:
                groups.append(e)
                current = e
                adj.remove(e)
                find_group(current, adj, groups)

if __name__ == '__main__':

    main()