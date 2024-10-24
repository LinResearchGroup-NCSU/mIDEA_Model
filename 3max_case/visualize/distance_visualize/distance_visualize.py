import re
import matplotlib.pyplot as plt

def parse_residues(file_content):
    pattern = r'<Residue (\w+) het=  resseq=(\d+) icode= >'
    
    matches = re.findall(pattern, file_content)
    
    residue_dict = {int(resseq): res for res, resseq in matches}
    
    return residue_dict

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content

def plot_5CM_distance(distance_data, residue_list, cutoff):
    distances = []
    for line in distance_data.strip().split('\n'):
        parts = line.split()
        resseq1, resseq2, distance = int(parts[0]) + 1, int(parts[1]) + 1, float(parts[2]) if float(parts[2]) <= cutoff else None #Transfer the idx to num
        if residue_list[resseq1] == '5CM' or residue_list[resseq2] == '5CM':
            other_resseq = residue_list[resseq2] if residue_list[resseq1] == '5CM' else residue_list[resseq1]
            distances.append((other_resseq, distance))

    res, distance_values = zip(*distances)

    plt.figure(figsize=(10,8))
    plt.scatter(res, distance_values,s=5)
    plt.xlabel('Residue Sequence Number')
    plt.ylabel('Distance to 5CM')
    plt.title('Distances to 5CM')
    plt.show()


def main():
    filename = '5ef6_res_list_entire.txt'

    file_content = read_file(filename)

    residue_list = parse_residues(file_content)
    # print(residue_list)

    distance_file_name = '5ef6_combined_residue_pairs_distances.txt'
    distance_content = read_file(distance_file_name)

    cutoff = 1.2
    plot_5CM_distance(distance_content, residue_list, cutoff)

if __name__ == "__main__":
    main()