# mIDEA: An Interpretable Structure–Sequence Model for Methylation-Dependent Protein–DNA Binding Sensitivity

**mIDEA** (Methylation-informed Interpretable protein–DNA Energy Associative model) is a structure-based, residue-level biophysical framework for predicting and interpreting methylation-dependent protein–DNA binding specificity. mIDEA extends a classical 20×4 amino acid–nucleotide interaction matrix by introducing **5-methylcytosine (5mC)** as the fifth nucleotide, expanding the matrix to **20×5**. This enables explicit modeling of methylation effects on protein–DNA interactions.

By integrating structural information from experimentally resolved or AI-predicted protein–DNA complexes with high-throughput methylation-dependent binding data, mIDEA provides both predictive accuracy and residue-level mechanistic insight. The model is trained using **two complementary strategies**:

**(i) Structure-informed optimization strategy**  
Combines structural templates, synthetic sequence decoys, and prior knowledge of how cytosine methylation modulates protein–DNA interactions to construct a sparse yet comprehensive training dataset. This allows the model to capture methylation effects even in the absence of quantitative measurements.

**(ii) Fully data-driven strategy**  
Directly fits the residue–nucleotide interaction matrix γ(a, n) using quantitative protein–methylated DNA binding data. Experimental signals are mapped onto geometric features of the protein–DNA interface to yield a more direct representation of methylation-dependent interaction patterns.

This repository demonstrates the modeling of the strong *methyl-minus* specificity of the MAX transcription factor using **strategy (i)**, the primary optimization approach in mIDEA.  

**Note**. Essential resources (implementation of strategy (ii), representative results, and visualization scripts) are provided in the RAW/ archive. Owing to GitHub’s file size restrictions, some intermediate data and auxiliary code are not included but can be made available upon request.

---

## Model Capabilities

- Train residue-level energy models using structural templates and synthetic sequence decoys  
- Predict binding free energies for unmethylated and methylated DNA sequences  
- Visualize γ interaction matrices and φ (residue–nucleotide contact) matrices  

---

## Repository Contents

- Implementation of both optimization strategies **(i)** and **(ii)**  
- Key raw data and figures   
- Visualization scripts  

---

## Installation

### Requirements
- Python 3  
- Conda (recommended)

### Setup

#### 1. Install Miniconda
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

### 1. Training the Energy Model γ

We train mIDEA using the MAX–DNA co-complex (PDB ID: 1HLO) as the structural template. To encode MAX's strong methyl-minus effect, the training set consists of a 10:1 ratio of unmethylated to methylated sequences:

- **Unmethylated:** `5'-CACCACGTGGT-3'`
- **Methylated:** `5'-CACCA(5mC)GTGGT-3'`

Both sequence types are threaded onto the structural template to construct the final training structures.

---

### 2. Prepare Input Files

**`proteinList.txt`**

Create `training/proteinList.txt` containing:
```text
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
- Naming format: `{PDB ID}_modified.pdb`  
- Chain names:  
  - Protein → `A`  
  - DNA → `B` and `C`

### 3. Run Training
```bash
cd training
bash train.sh
```

### 4. Configuration Options

**Interaction Atoms**
Edit `get_interaction_atom` in `common_functions/common_function.py` to define coarse-grained interaction atoms.

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
optimization/for_training_gamma/optimize_gamma.py
```

Set:
```python
cutoff_mode = 60
```
Retains the largest 60 eigenvalues.

### 5. Output

Training results are stored in:
```
training/optimization/for_training_gamma/gammas/randomized_decoy/
```

**Key file** (final filtered γ energy matrix):
```
native_trainSetFiles_phi_pairwise_contact_well-8.0_8.0_0.7_10_gamma_filtered
```

### 6. Visualization

Visualize the trained energy model with:
```bash
cd training/optimization/for_training_gamma/
python visualize.py
```

Figures are saved in:
```
training/optimization/for_training_gamma/visualize/
```

**Includes:**
- optimized γ interaction matrix  
- native φ contact matrix  
- averaged decoy φ matrix

### 7. Predicting Protein–DNA Binding Free Energies

We first generate testing φ matrices for both the methylated and unmethylated versions of the testing sequences.

1. **Prepare Input Files**
   - Place PDB files in `testing/PDBs/`
   - DNA testing sequences are in `testing/sequences/`
   - Use `dna_half.seq` as input  
     Optionally, run:
     ```bash
     python reverse_complement.py
     python merge.py
     ```
     to generate full double-stranded DNA sequences
   - Ensure the sequence length matches the native PDB structure

2. **Treat CpG as methylated**  
   In `testing/mapDNAseq_reverse.py`, set:
   ```python
   handle_CG = True


3. **Generate Testing φ**:
   ```bash
   cd testing/
   bash test.sh 1hlo
   ```
   - Output in `testing/phis`:
     - `phi_pairwise_contact_well_native_decoys_CPLEX_randomization_-8.0_8.0_0.7_10` (φ for testing sequences).

4. **Calculate binding energy**
- Copy and rename the generated γ and φ files into `testing/phis/`
- Then compute the predicted energies using:
  ```bash
  python calculate_predicted_energy.py # using E = γφ (remember to update the file name in the script)
  ```

## Supplementary Materials
- **Implementation of strategy (ii):** `RAW/Strategy2/`
- **Key results and visualization code:** `RAW/Data/`
- **Raw figures (editable):** `RAW/Figures/`

## References

Yafan Zhang, Rina Li, Junhao Zhong, and Xingcheng Lin.  
“mIDEA: An Interpretable Structure–Sequence Model for Methylation-Dependent Protein–DNA Binding Sensitivity”.  
*bioRxiv* (2025). DOI: https://doi.org/10.1101/2025.11.14.688575

## Contact

For questions or support, contact the [Lin Research Group](https://lingroup.wordpress.ncsu.edu/) or open an issue on GitHub.
