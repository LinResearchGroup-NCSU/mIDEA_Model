import re
import matplotlib.pyplot as plt

three_to_one_letter = {
    'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E', 'PHE': 'F',
    'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LYS': 'K', 'LEU': 'L',
    'MET': 'M', 'ASN': 'N', 'PRO': 'P', 'GLN': 'Q', 'ARG': 'R',
    'SER': 'S', 'THR': 'T', 'VAL': 'V', 'TRP': 'W', 'TYR': 'Y',
    '5CM': '5CM'  
}

def parse_residues(file_content):
    pattern = r'<Residue (\w+) het=  resseq=(\d+) icode= >'
    
    matches = re.findall(pattern, file_content)
    
    residue_dict = {int(resseq): three_to_one_letter.get(res, res) for res, resseq in matches}
    
    return residue_dict

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content

def plot_5CM_distance(distance_data, residue_list, cutoff):
    distances = []
    res_count = {}
    for line in distance_data.strip().split('\n'):
        parts = line.split()
        resseq1, resseq2, distance = int(parts[0]) + 1, int(parts[1]) + 1, float(parts[2]) if float(parts[2]) <= cutoff else None  
        if distance is not None and (residue_list.get(resseq1) == '5CM' or residue_list.get(resseq2) == '5CM'):
            other_resseq = residue_list.get(resseq2) if residue_list.get(resseq1) == '5CM' else residue_list.get(resseq1)
            distances.append((other_resseq, distance))
            
            if other_resseq not in res_count:
                res_count[other_resseq] = 0
            res_count[other_resseq] += 1

    if distances:
        res, distance_values = zip(*distances)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        ax1.bar(res_count.keys(), res_count.values(), alpha=0.6)
        ax1.set_xlabel('Residue (Single Letter)')
        ax1.set_ylabel('Number of Data Points')
        ax1.set_title('Data Points per Residue')

        ax2.scatter(res, distance_values, s=3)
        ax2.set_xlabel('Residue (Single Letter)')
        ax2.set_ylabel('Distance to 5CM')
        ax2.set_title('Distances to 5CM')

        plt.tight_layout()
        plt.savefig('residue_distances_plot.png', format='png')
    else:
        print("No valid distances found to plot.")

def main():
    filename = '5ef6_res_list_entire.txt'
    file_content = read_file(filename)
    
    residue_list = parse_residues(file_content)

    distance_file_name = '5ef6_combined_residue_pairs_distances.txt'
    distance_content = read_file(distance_file_name)

    cutoff = 1.2
    plot_5CM_distance(distance_content, residue_list, cutoff)

if __name__ == "__main__":
    main()
