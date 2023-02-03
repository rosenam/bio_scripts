#!/usr/bin/env python3

"""
Austin Rosen

Rosalind Find Protein Motifs Problem

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif,
    output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import argparse
import urllib.request

def supply_args():

    # parse command line for arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_file', help='Input file of UniProt IDs')
    args = parser.parse_args()

    return args
def main():

    args = supply_args()

    # create url with id name
    with open(args.input_file) as in_file:
        for line in in_file:
            name = line.rstrip()
            chunks = line.rstrip().split('_')
            id = chunks[0]
            url = 'https://rest.uniprot.org/uniprotkb/' + id + '.fasta'

            # open url
            with urllib.request.urlopen(url) as webUrl:
                i = 0
                aa = ''
                indices = ''
                found = False

                # turn url into aa sequence
                for line in webUrl:
                    if i != 0:
                        line = str(line.rstrip())
                        line = line[2:-1]
                        aa = aa + line
                    i += 1

                # search for given protein motif
                for e in range(len(aa) - 3):
                    if aa[e] == 'N' and aa[e+1] != 'P':
                        if aa[e+2] == 'S' or aa[e+2] == 'T':
                            if aa[e+3] != 'P':
                                indices += str(e+1) + ' '
                                found = True

                # print location if motif found
                if found == True:
                    print(name)
                    print(indices.rstrip())


    return

if __name__ == "__main__":

    main()