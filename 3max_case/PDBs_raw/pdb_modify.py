import sys

def remove_ter_and_renumber_atoms(pdb_id):
    input_pdb = f'{pdb_id}.pdb'
    output_pdb = f'{pdb_id}_modified.pdb'

    # Initialize counters for atoms and residues
    atom_counter = 1
    residue_counter = 1
    current_residue_number = None
    
    # Store lines separately for protein and DNA
    protein_lines = []
    dna_lines = []
    
    # First pass: separate lines by chain type
    with open(input_pdb, 'r') as infile:
        for line in infile:
            if (line.startswith('ATOM') or line.startswith('HETATM')) and not " HOH " in line:
                res_name = line[17:20].strip()
                if res_name in ['DA', 'DT', 'DG', 'DC', '5CM']:  # DNA residues
                    dna_lines.append(line)
                else:  # Protein residues
                    protein_lines.append(line)
    
    # Second pass: process protein lines and then DNA lines
    with open(output_pdb, 'w') as outfile:
        # Process protein lines first
        for line in protein_lines:
            serial_number = str(atom_counter).rjust(5)
            line = 'ATOM  ' + line[6:]  # Change HETATM to ATOM if necessary
            line = line[:6] + serial_number + line[11:]
            
            # Check if the residue number has changed
            residue_number = line[22:26].strip()
            if residue_number != current_residue_number:
                current_residue_number = residue_number
                new_res_number = str(residue_counter).rjust(4)
                residue_counter += 1
            else:
                new_res_number = str(residue_counter - 1).rjust(4)
            
            line = line[:22] + new_res_number + line[26:]
            atom_counter += 1
            outfile.write(line)
        
        # Process DNA lines after protein lines
        for line in dna_lines:
            serial_number = str(atom_counter).rjust(5)
            line = 'ATOM  ' + line[6:]  # Change HETATM to ATOM if necessary
            line = line[:6] + serial_number + line[11:]
            
            # Check if the residue number has changed
            residue_number = line[22:26].strip()
            if residue_number != current_residue_number:
                current_residue_number = residue_number
                new_res_number = str(residue_counter).rjust(4)
                residue_counter += 1
            else:
                new_res_number = str(residue_counter - 1).rjust(4)
            
            line = line[:22] + new_res_number + line[26:]
            atom_counter += 1
            outfile.write(line)

if __name__ == "__main__":
    pdb_id = sys.argv[1]
    remove_ter_and_renumber_atoms(pdb_id)
