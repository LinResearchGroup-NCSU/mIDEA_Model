# mIDEA: An Interpretable Structure–Sequence Model for Methylation-Dependent Protein–DNA Binding Sensitivity

mIDEA (Methylation-informed Interpretable protein–DNA Energy Associative model) is a structure-based, residue-level biophysical framework for predicting and interpreting methylation-dependent protein–DNA binding specificity. mIDEA extends a classical 20×4 amino acid–nucleotide interaction matrix by introducing **5-methylcytosine (5mC)** as a fifth nucleotide type, expanding the interaction matrix to **20×5**. This design enables explicit modeling of methylation effects on protein–DNA energetics.

By integrating structural information from experimentally resolved or AI-predicted protein–DNA complexes with high-throughput methylation-dependent binding data, mIDEA provides both predictive accuracy and residue-level mechanistic insight.

This repository demonstrates how to model the strong *methyl-minus* specificity of the MAX transcription factor using mIDEA.

## Features

- Train residue-level energy models based on structural templates
- Predict binding free energies of unmethylated and methylated DNA sequences
- Visualize γ-matrices and φ contact matrices

## Installation

### Requirements
- Python 3
- Conda (recommended)

### Setup

**1. Install Miniconda:**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

**2. Clone the repository:**
```bash
git clone https://github.com/LinResearchGroup-NCSU/mIDEA_Model
```

**3. Create and activate the environment:**
```bash
cd mIDEA_Model
conda env create -f mIDEA.yaml -n mIDEA
conda activate mIDEA
```

**4. Make scripts executable:**
```bash
chmod +x *.sh
```

## Usage

### 1. Training the Energy Model

We train mIDEA using the MAX–DNA co-complex (PDB ID: 1HLO) as the structural template. To encode MAX's strong methyl-minus effect, the training set consists of a 10:1 ratio of unmethylated to methylated sequences:

- **Unmethylated**: 5'-CACCACGTGGT-3'
- **Methylated**: 5'-CACCA(5mC)GTGGT-3'

Both sequence types are threaded onto the structural template.

### 2. Prepare Input Files

**proteinList.txt**
Create `training/proteinList.txt` containing:
```
1hloun00
1hloun01
1hloun02
1hloun03
1hloun04
1hloun05
1hloun06
1hloun07
1hloun08
1hloun09
1hlom00
```

**PDB files**
- Place files under: `training/PDBs/`
- Naming: `{PDB ID}_modified.pdb`
- Chain names:
  - Protein → A
  - DNA → B and C

### 3. Run Training
```bash
bash train.sh
```

### 4. Configuration Options

**Interaction Atoms**
Edit `get_interaction_atom` in `common_function.py` to define coarse-grained interaction atoms.

*Manuscript defaults:*
- Protein residues → Cα (CA)
- DNA → phosphate (P)

**Decoy Generation**
Decoys are generated in:
```bash
training/optimization/for_bindingE/template/sequences/
```

*Defaults:*
- Protein decoys → 10,000
- DNA decoys → 1,000

**Eigenvalue Cutoff**
In:
```bash
training/optimization/for_training_gamma/optimize_gamma.py
```

Set:
```python
cutoff_mode = 60
```
Retains the largest 60 eigenvalues for γ-regularization.

### 5. Output

Training results are stored in:
```
training/optimization/for_training_gamma/gammas/randomized_decoy/
```

**Key file** (final γ energy matrix):
```
native_trainSetFiles_phi_pairwise_contact_well-8.0_8.0_0.7_10_gamma_filtered
```

### 6. Visualization

Generate model figures with:
```bash
cd training/optimization/for_training_gamma/
python visualize.py
```

Outputs are saved in:
```
training/optimization/for_training_gamma/visualize/
```

**Includes:**
- γ interaction matrix
- native φ contact matrix  
- averaged decoy φ matrix
```

Below need to be changed:

### Predicting Protein-DNA Binding Free Energies 

Generate phi values and calculate binding energies for given testing binders (e.g., Max 255 mutated binders testing dataset in Maerkl, S. J et al.).

1. **Prepare Input Files**:
   - Place PDB files in `testing/PDBs`.
   - DNA (testing) sequences are in `testing/sequences`.

2. **Generate Testing Sequences**:
   - Use `dna_half.seq` as input. Optionally, run `reverse_complement.py` and `merge.py` to generate full double-stranded DNA sequences.
   - Ensure the length of sequences matches the native PDB structure.

3. **Generate Testing Phi**:
   ```bash
   cd testing/
   bash test.sh 1hlo
   ```
   - Output in `testing/phis`:
     - `phi_pairwise_contact_well_native_decoys_CPLEX_randomization_-8.0_8.0_0.7_10` (255 lines for testing sequences).
     - `phi_pairwise_contact_well_native_native_-8.0_8.0_0.7_10` (1 line for native structure).

4. **Calculate Binding Energy**:
   - Copy the files to `energy_calculation/`:
     ```bash
     cp training/optimization/for_training_gamma/gammas/randomized_decoy/native_trainSetFiles_phi_pairwise_contact_well-8.0_8.0_0.7_10_gamma_filtered energy_calculation/
     cp testing/phis/phi_pairwise_contact_well_native_decoys_CPLEX_randomization_-8.0_8.0_0.7_10 energy_calculation/
     ```
   
   - Navigate to `energy_calculation` and run:
     ```bash
     python calculate_testing_energy.py
     ```
   - Output: `Energy_mg.txt` (predicted energies using **E = γΦ**).

## Supplementary Materials

- **Trained Energy Models**: [IDEA_trained_energy_models](https://github.com/LinResearchGroup-NCSU/IDEA_Model/tree/main/supplementary_materials/IDEA_trained_energy_models)
- **Raw Data**: [raw_data.zip](https://github.com/LinResearchGroup-NCSU/IDEA_Model/blob/main/supplementary_materials/raw_data.zip)
- **Processed Published Models**: Scripts for comparing with DBD-hunter and rCLAMPS: [other_published_models](https://github.com/LinResearchGroup-NCSU/IDEA_Model/tree/main/supplementary_materials/other_published_models)

## References

- Zhang, Y., Silvernail, I., Lin, Z., & Lin, X. (2025). Interpretable Protein–DNA Interactions Captured by Structure–Sequence Optimization. eLife, 14, e105565. https://doi.org/10.7554/eLife.105565
- Maerkl, S. J., & Quake, S. R. (2007). A Systems Approach to Measuring the Binding Energy Landscapes of Transcription Factors. *Science*, 315(5809), 233–237. [DOI:10.1126/science.1131007](https://doi.org/10.1126/science.1131007)

## Contact

For questions or support, contact the [Lin Research Group](https://lingroup.wordpress.ncsu.edu/) or open an issue on GitHub.
