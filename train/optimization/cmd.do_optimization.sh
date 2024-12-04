#########################################################################
# Author: Xingcheng Lin
# Created Time: Sat Feb 13 19:56:33 2021
# File Name: cmd.do_optimization.sh
# Description: 
#########################################################################
#!/bin/bash

cd for_bindingE/

# Run to generate phi file
echo "bash cmd.for_phi.sh"
bash cmd.for_phi.sh
echo "bash cmd.for_phi.sh finished"

# Copy the generated phi into the loocv folder
echo "cmd.copyFile.sh"
cd loocv/
bash cmd.copyFile.sh
echo "cmd.copyFile.sh finished"
cd ../../

# Do the training;
echo "cmd.training.sh"
bash cmd.training.sh
echo "cmd.training.sh finished"

# Delete the target folder for saving space, only delete after training is complete
# bash cmd.delete.sh

cd ../
