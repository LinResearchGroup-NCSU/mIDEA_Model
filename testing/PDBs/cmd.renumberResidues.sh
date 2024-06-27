#########################################################################
# Author: Xingcheng Lin
# Created Time: Fri Dec 13 17:16:06 2019
# File Name: cmd.do_analysis.sh
# Description: 
#########################################################################
#!/bin/bash

while read f
do
    echo $f
    ModifyPDBFiles.pl --mode RenameChainIDs --ChainIDStart A $f.pdb
    ModifyPDBFiles.pl --mode RenumberResidues --ResidueNumberMode Sequential ${f}RenameChainIDs.pdb
    mv ${f}RenameChainIDsRenumberResidues.pdb ${f}_modified.pdb
done < proteinList.txt
