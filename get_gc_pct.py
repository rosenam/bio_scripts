"""
Takes DRAGEN fastqc metrics file and computes gc pct for R1 and R2

Austin Rosen
"""

import argparse
def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("metrics", help="fastqc metrics file")
    args = parser.parse_args()
    return args
def main():

    args = argparser()

    print(args.metrics)

    R1_reads = 0
    R2_reads = 0
    R1_G = 0
    R1_C = 0
    R2_G = 0
    R2_C = 0

    # sum values of interest from dragen output file
    with open(args.metrics) as in_handle:
        for line in in_handle:
            if "POSITIONAL BASE CONTENT" in line:
                if "Read1" in line:
                    R1_reads += int(line.split(',')[3])
                    if "G Bases" in line:
                        R1_G += int(line.split(',')[3])
                    if "C Bases" in line:
                        R1_C += int(line.split(',')[3])
                if "Read2" in line:
                    R2_reads += int(line.split(',')[3])
                    if "G Bases" in line:
                        R2_G += int(line.split(',')[3])
                    if "C Bases" in line:
                        R2_C += int(line.split(',')[3])

    # compute GC for R1 and R2 
    gc_r1 = (R1_G + R1_C) / R1_reads
    gc_r2 = (R2_G + R2_C) / R2_reads

    print(gc_r1, gc_r2)

if __name__ == "__main__":

    main()