"""
Austin Rosen

Conditions and Loops -- Rosalind Exercise
"""

def main():

    a = 4428
    b = 8736
    ans = 0

    if a % 2 == 0: a = a + 1
    if b % 2 == 1: b = b + 1

    for i in range(a,b,2):
        ans = ans + i

    print(ans)

if __name__ == "__main__":

    main()