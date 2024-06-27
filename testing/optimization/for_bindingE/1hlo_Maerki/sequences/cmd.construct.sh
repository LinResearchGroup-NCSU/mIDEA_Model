
# Start with half DNA with the interested sequences
python reverse_complement.py dna_half.seq dna_half_complement.seq
# Concatenate dna_half.seq and dna_half_complement.seq to be dna.seq
python mapDNAseq_reverse.py dna.seq dna_modeller.seq
# Copy and paste the sequences in dna_modeller.seq to CPLEX_randomization/native.decoy
cd ../
python evaluate_phi.py


 
