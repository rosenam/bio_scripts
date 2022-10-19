# -*- coding: utf-8 -*-
"""
Austin Rosen
Binary Search Algorithm
"""
##################################
def main(n,m,k,l):
    
    '''
    This function makes calls to the binary search algorithm,
    and writes the output to a file.
    '''
    
    out_handle = open("binary_search_results.txt", "w")
    for num in l:
        binary(k,k,num,out_handle)
    return

##################################
    
def binary(k,tmp,num,out_handle):
    
    '''
    This function performs the binary search, with recursive calls to the function
    '''
    
    n = len(tmp)            # find length of array
    half = int(n/2)         # find index for the midpoint of the array
    if n == 0:              # if array is empty, answer is -1
        print(-1)
        out_handle.write("-1 ")
        return
    elif n == 1:            # if array has a single value, check if key equals array value
        if num == tmp[0]:
            print(k.index(num) + 1)
            out_handle.write(str(k.index(num) + 1) + " ")
            return
        else:
            print(-1)
            out_handle.write("-1 ")
            return 
    else:                   # check if the key is greater than, less than, or equal to the midpoint value of the array
        if num == tmp[half]:            # if equal, return array index
            print(k.index(num) + 1)
            out_handle.write(str(k.index(num) + 1) + " ")
            return
        elif num < tmp[half]:           # if less than, repeat algorithm
            new_tmp = tmp[:half]        
            binary(k, new_tmp, num, out_handle)
        elif num > tmp[half]:           # if greater than, repeat algorithm
            new_tmp = tmp[half+1:]
            binary(k, new_tmp, num, out_handle)
      
####################################     
            
if __name__ == "__main__":
    
    in_handle = open("rosalind_bins_test.txt")      # read in data
    
    with in_handle:             # turn data into proper format for the main() function
        data = [0,0,0,0]
        i = 0
        for line in in_handle:
            data[i] = line.rstrip()
            i += 1
        n = data[0]
        m = data[1]
        k = data[2].split()
        l = data[3].split()
        
        main(n,m,k,l)

###########################################