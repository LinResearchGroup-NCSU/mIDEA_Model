#########################################################################
# Author: Xingcheng Lin
# Created Time: Sun Dec  5 11:18:36 2021
# File Name: cmd.copyprotein_list.sh
# Description: proteins_list.txt includes all the strong binder labels and the template PDB
#########################################################################
#!/bin/bash

tail -n +0 proteins_list.txt >  ./optimization/proteins_list.txt
tail -n +0 proteins_list.txt > ./optimization/for_bindingE/proteins_list.txt
tail -n +0 proteins_list.txt > ./optimization/for_bindingE/loocv/proteins_list.txt
tail -n +0 proteins_list.txt > ./optimization/for_training_gamma/proteins_list.txt
tail -n +0 proteins_list.txt > ./optimization/for_training_gamma/phis/proteins_list.txt

# In the structure file, we need to add the template PDB
cp proteins_list.txt structures/modeller/


# We copy the updated phi1 parameters into the protocol
cp phi1_list.txt ./optimization/for_training_gamma/
cp phi1_list.txt ./optimization/for_bindingE/template/
cp phi1_list.txt ./optimization/for_bindingE/loocv/
