#########################################################################
# Author: Xingcheng Lin
# Created Time: Wed Jun 17 21:56:01 2020
# File Name: cmd.copyFile.sh
# Description: Copy the structure, phis and tms files from each folder built in for_bindingE/ 
# into the corresponding folders in this directory for training
#########################################################################
#!/bin/bash

while read f
do
    echo $f
    cp ../for_bindingE/1hlo/native_structures_pdbs_with_virtual_cbs/${f}.pdb native_structures_pdbs_with_virtual_cbs/${f}.pdb
    cp ../for_bindingE/1hlo/phis/phi_pairwise_contact_well_${f}_native_-1.0_9.5_5.0_10 phis/phi_pairwise_contact_well_${f}_native_-1.0_9.5_5.0_10
    cp ../for_bindingE/1hlo/phis/phi_pairwise_contact_well_${f}_decoys_CPLEX_randomization_-1.0_9.5_5.0_10 phis/phi_pairwise_contact_well_${f}_decoys_CPLEX_randomization_-1.0_9.5_5.0_10
    cp ../for_bindingE/1hlo/tms/${f}.tm tms/${f}.tm
done < native_trainSetFiles.txt
