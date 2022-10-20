# -*- coding: utf-8 -*-
"""
Austin Rosen

Dominant Allele Probability Calculator (Rosalind Exercise)
"""
####################################
def main(hom,het,rec):
    
    '''
    
    This function computes the probability that the offspring of two randomly selected
    mates from a population (consisting of m, n, and k individuals) contains
    a dominant allele
    
    '''
    
    tot = hom + het + rec
    
    pr_dom = hom/tot + (het/tot)*((hom)/(tot-1)) + (rec/tot)*(hom/(tot-1)) + (rec/tot)*(het/(tot-1)) + 0.75*(het/tot)*((het-1)/(tot-1))
    
    pr_dom = round(pr_dom, 5)

    return(pr_dom)

######################################
if __name__ == '__main__':
    
    print(main(21,29,23))

#####################################