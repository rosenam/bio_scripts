"""
Austin Rosen

Sex Linked Inheritance -- Rosalind Problem
"""

def main():

    in_handle = open("sex_linked.txt")
    for line in in_handle:
        vals = line.split()

    print(*vals)

    results = []
    for p in vals:
        p = float(p)
        ans = 2 * p * (1 - p)
        results.append(round(ans,3))

    print(*results)
if __name__ == "__main__":

    main()