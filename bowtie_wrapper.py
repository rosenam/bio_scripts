# -*- coding: utf-8 -*-
"""
Austin Rosen
Bowtie Wrapper

"""

import argparse

######################################

def main():
   input_file, output_file, index_path = arg_parse()
   trimm(input_file, output_file)
   bowtie_in = output_file
   bowtie(index_path, bowtie_in)
   
########################################   
    
def arg_parse():
    
    '''
    Parse command line arguments
    '''
    
    # First we need to create an instance of ArgumentParser which we will call parser:
    parser = argparse.ArgumentParser()
    
    # The add_argument() method is called for each argument:
    # We provide two version of each argument: 
    # -a is the shortand, --sequence1 is the longhand
    # We can specify a help message describing the argument with help="message"
    # To require an argument, we use required=True
    parser.add_argument('-i', '--infile', required=True, help="fastq file") 
    parser.add_argument('-o', '--output', required=True, help="trimmed file")
    parser.add_argument('-x', '--index_path', required=True, help="path to bowtie index")
    
    # The parse_args() method parses the arguments
    args = parser.parse_args()
    print('args:', args)
    
    # Here, we'll return the arguments as a tuple
    return args.infile, args.output, args.index_path

########################################################

def trimm(infile, output):
    
    '''
    This function calls the trimmomatic software with the specfied input/ouput and writes a log file
    '''
    
    try:
        log_handle = open('log', 'w')
    except:
        return -1
    
    with log_handle:
        process = subprocess.run(['trimmomatic', 'SE', infile, output, 'ILLUMINACLIP:TruSeq-smallRNA.fa:2:30:10', 'MINLEN:16 AVGQUAL:30'], stdout=subprocess.PIPE)
        log_handle.write("trimmomatic\n" + process.stdout.decode('utf-8') + process.stderr.decode('utf-8') + "\n")

######################################################

def bowtie(bowtie_path, fastq_file):
    
    '''
    This function calls bowtie software and supplies fastq files for input
    '''
    
    try:
        log_handle = open('log', 'a')
    except:
        return -1
    with log_handle:
        process = subproces.run(['bowtie2', '-x', bowtie_path, '-U', fastq_file, '-S', 'output.sam'])

########################################
    
if __name__ == '__main__':
    main()
