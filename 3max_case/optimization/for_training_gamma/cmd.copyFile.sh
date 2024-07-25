#########################################################################
# Author: Xingcheng Lin
# Created Time: Wed Jun 17 21:56:01 2020
# File Name: cmd.copyFile.sh
# Description: Copy the structure, phis and tms files from each folder built in for_bindingE/ 
# into the corresponding folders in this directory for training
#########################################################################
#!/bin/bash

# Use grep and awk to extract the required parameters

params=$(grep -v "^#" phi1_list.txt | grep "phi_pairwise_contact_well" | awk '{print $2"_"$3"_"_$4"_"$5}')

echo "Extracted params: $params"

while read f
do
    echo $f
    echo "Copying ../for_bindingE/$f/native_structures_pdbs_with_virtual_cbs/native.pdb to native_structures_pdbs_with_virtual_cbs/${f}.pdb"
    cp ../for_bindingE/$f/native_structures_pdbs_with_virtual_cbs/native.pdb native_structures_pdbs_with_virtual_cbs/${f}.pdb

    echo "Copying ../for_bindingE/$f/phis/phi_pairwise_contact_well_native_native_${params} to phis/phi_pairwise_contact_well_${f}_native_${params}"
    cp ../for_bindingE/$f/phis/phi_pairwise_contact_well_native_native_${params} phis/phi_pairwise_contact_well_${f}_native_${params}
    
    echo "Copying ../for_bindingE/$f/phis/phi_pairwise_contact_well_native_decoys_CPLEX_randomization_${params} to phis/phi_pairwise_contact_well_${f}_decoys_CPLEX_randomization_${params}"
    cp ../for_bindingE/$f/phis/phi_pairwise_contact_well_native_decoys_CPLEX_randomization_${params} phis/phi_pairwise_contact_well_${f}_decoys_CPLEX_randomization_${params}
    
    # echo "Copying ../for_bindingE/$f/tms/${f}.tm to tms/${f}.tm"
    # cp ../for_bindingE/$f/tms/${f}.tm tms/${f}.tm
done < native_trainSetFiles.txt




