###########################################################################
# This script will map DNA sequence from the output of Modeller to real
# Modified to handle special CG mapping rules with middle position exception
#
# Written by Xingcheng Lin, 12/12/2016;
# Modified by Yafan Zhang, 12/05/2024;
###########################################################################

# Set this to True if you want to apply the C in CG to "." rule, or False to skip it
handle_CG = True

import sys

def mapDNAseq_reverse(DNAseq_file, outputFile):
    # Dictionary between real DNA bases and Modeller representation
    Real_to_Modeller = {
        "A": "e",
        "G": "l",
        "C": "j",
        "T": "t"
    }

    infile = open(DNAseq_file, 'r')
    outfile = open(outputFile, 'w')

    # Read in lines from the file
    lines = [line.strip() for line in infile]
    infile.close()

    for line in lines:
        seq = list(line)  # Convert string to list for character-by-character processing
        seq_length = len(seq)
        real_seq = []

        # Determine middle positions
        if seq_length % 2 == 0:
            middle_positions = [seq_length // 2 - 1, seq_length // 2]
        else:
            middle_positions = [seq_length // 2]

        for idx in range(seq_length):
            base = seq[idx]
            # If CG-handling is enabled and we see a "C" followed by "G"
            if handle_CG and base == "C" and idx + 1 < seq_length and seq[idx + 1] == "G":
                # If this "C" is not at a middle position, map to "."
                if idx not in middle_positions:
                    real_seq.append(".")
                    continue
                # Otherwise (it is in the middle), fall through to normal mapping

            # Normal mapping for all other cases (or if handle_CG is False)
            real_seq.append(Real_to_Modeller.get(base, base))

        converted_seq = "".join(real_seq)
        outfile.write(converted_seq + "\n")

    outfile.close()
    return

############################################################################

if __name__ == "__main__":
    dnaSeq_file = sys.argv[1]
    outputFile = sys.argv[2]

    mapDNAseq_reverse(dnaSeq_file, outputFile)
    print("[INFO] Testing sequences mapping complete. CG handling =", handle_CG)

   # print("When the voice of the Silent touches my words,")
   # print("I know him and therefore know myself.")
