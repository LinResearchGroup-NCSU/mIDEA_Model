cd PDBs_raw/

sed -i 's/\r//' proteinList.txt  
sed -i '/^$/d' proteinList.txt   
#!/bin/bash

while IFS= read -r f || [ -n "$f" ]; do
    echo $f 
    pdb_id=$(echo $f | tr -d '\r')  # Remove any carriage return characters
    python pdb_modify.py $pdb_id
    cp ${pdb_id}_modified.pdb ../PDBs/ 
done < proteinList.txt



