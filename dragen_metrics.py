"""
Take DRAGEN metrics file (.json) and FastQC file (.csv) and report metrics of interest

Austin Rosen
"""


import argparse

def supply_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("fastqc", help="fastqc metrics file")
    parser.add_argument("json", help="json metrics file")
    args = parser.parse_args()
    return args

def main():

    args = supply_args()

    r1_reads, r2_reads = 0, 0
    r1_gc, r2_gc = 0, 0


    # sum values of interest from DRAGEN FastQC output file
    with open(args.fastqc) as qc_handle:
        for line in qc_handle:
            if "POSITIONAL BASE CONTENT" in line:
                num = int(line.split(',')[3])
                if "Read1" in line:
                    r1_reads += num
                    if "G Bases" in line or "C Bases" in line:
                        r1_gc += num
                if "Read2" in line:
                    r2_reads += num
                    if "G Bases" in line or "C Bases" in line:
                        r2_gc += num


    # compute GC content for R1 and R2
    gc_r1 = round(r1_gc * 100 / r1_reads, 2)
    gc_r2 = round(r2_gc * 100 / r2_reads, 2)

    # gather metrics of interest from DRAGEN metrics json
    with open(args.json, "r") as m_handle:
        for line in m_handle:
            line = line.strip().strip(",").replace("\"", "")
            if "q30_bases_pct" in line:
                q30 = line
            if "average_alignment_coverage_over_target_region" in line:
                avg_depth = line
            if "pct_of_target_region_with_coverage_10x_inf" in line:
                depth10 = line
            if "pct_of_target_region_with_coverage_20x_inf" in line:
                depth20 = line
            if "pct_of_target_region_with_coverage_50x_inf" in line:
                depth50= line
            if "pct_of_target_region_with_coverage_100x_inf" in line:
                depth100 = line
            if "aligned_reads_in_target_region_pct" in line:
                pct_on_target = line
            if "ploidy_estimation" in line:
                ploidy_est = line

    # print metrics of interest
    print(q30, avg_depth, depth10, depth20, depth50, depth100, pct_on_target, ploidy_est, sep="\n")
    print("gc_pct_r1:", gc_r1)
    print("gc_pct_r2:", gc_r2)

if __name__ == "__main__":

    main()