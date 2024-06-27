#########################################################################
# Author: Xingcheng Lin
# Created Time: Wed Jun 10 22:48:33 2020
# File Name: cmd.preprocessing.sh
# Description: 
#########################################################################
#!/bin/bash

export PDBid=$1
export protChain=$2

# Here, different complex has a different protein-DNA interface, so we need to deal with them separately;
rm -r sequences/DNA_randomization
mkdir -p sequences/DNA_randomization
#rm -r sequences/prot_randomization
#mkdir -p sequences/prot_randomization 
rm -r sequences/CPLEX_randomization
mkdir -p sequences/CPLEX_randomization
while read f
do  
    #  A temporary list for each protein;
    echo $f > proteins_tmp_list.txt

    # Add fake CB atoms, AWSEM format requirement
    cp ../traj_struct/${f}.pdb native_structures_pdbs_with_virtual_cbs/
 #   python add_fakeCB.py

    # Generate randomized sequence for the decoys;
    cp proteins_tmp_list.txt sequences/
    cp native_structures_pdbs_with_virtual_cbs/${f}.pdb sequences/
    cd sequences/

    # Build the sequence for native.pdb
    python buildseq.py ${f}
    bash cmd.cleanSequences.sh ${f}.seq
    cp ${f}.seq gBinder_sequences.txt 

    # Generate decoys for the DNA

    # Find the indices of contacting protein-DNA residues
    # Cutoff for determining contacting residues, unit: nm
    export cutoff=1.15
    python find_cm_residues.py ${f}.pdb $cutoff randomize_position_prot.txt randomize_position_DNA.txt

    cp randomize_position_DNA.txt ${f}.seq gBinder_sequences.txt DNA_randomization/

    python generate_decoy_seq_DNA.py


    ## Generate decoys for the protein
    #
    #cp randomize_position_prot.txt ${f}.seq gBinder_sequences.txt prot_randomization/
    #
    #python generate_decoy_seq_prot.py

    # Combine the generated DNA and protein decoys together
    cat DNA_randomization/${f}.decoys prot_randomization/${f}.decoys > CPLEX_randomization/${f}.decoys

    cd ../

    # Create the tms file, where the DNA is labeled as '2', while the protein are labeled as '1';
    grep "CA\|C5" native_structures_pdbs_with_virtual_cbs/${f}.pdb > tmp.txt
    # Get the total number of residues;

    tot_resnum=`cat tmp.txt | awk 'END{print $6}'`
    python create_tms.py sequences/DNA_randomization/randomize_position_DNA.txt $tot_resnum ${f}.tm

done < proteins_list.txt

gsed "s/CPLEX_NAME/$PDBid/g; s/PROT_CHAIN/$protChain/g" template_evaluate_phi.py > evaluate_phi.py
python evaluate_phi.py
