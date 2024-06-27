###########################################################################
# This script will map DNA sequence from the output of Modeller to real
#
# Written by Xingcheng Lin, 12/12/2016;
###########################################################################

import time
import subprocess
import os
import math
import sys
import numpy as np

################################################


def my_lt_range(start, end, step):
    while start < end:
        yield start
        start += step


def my_le_range(start, end, step):
    while start <= end:
        yield start
        start += step
#############################################


def mapDNAseq(DNAseq):

    # Dictionary between Modeller to Real DNA sequence;
    Modeller_to_Real = {
            "e": "A",
            "l": "G",
            "j": "C",
            "t": "T"
            }

    seq = list(DNAseq)
    real_seq = []

    for i in my_lt_range(0, len(seq), 1):
        real_seq.append(Modeller_to_Real[seq[i]])


    print(('').join(real_seq))

    return


############################################################################

if __name__ == "__main__":
    dnaSeq = sys.argv[1]

    mapDNAseq(dnaSeq)
    print("When the voice of the Silent touches my words,")
    print("I know him and therefore know myself.")
