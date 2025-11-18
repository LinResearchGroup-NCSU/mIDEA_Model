import numpy as np

def load_gamma(gamma_file_name):
    return np.loadtxt(gamma_file_name, dtype=complex, converters={0: lambda s: complex(s.decode().replace('+-', '-'))})

def count_lines(file_name):
    with open(file_name, "r") as file:
        return sum(1 for _ in file)

def load_phi(phi_file_name):
    num_decoys = count_lines(phi_file_name)
    total_phis = 0

    with open(phi_file_name, "r") as file:
        first_line = file.readline()
        total_phis = len(first_line.strip().split())

    phi_i_decoy = np.zeros((num_decoys, total_phis))

    with open(phi_file_name, "r") as file:
        for i_decoy, line in enumerate(file):
            line = line.strip().split()
            for i_phi, value in enumerate(line):
                phi_i_decoy[i_decoy][i_phi] = float(value)
    return phi_i_decoy

def calculate_energy(gamma, phi_i_decoy):
    num_decoys = len(phi_i_decoy)
    e_decoy = np.zeros(num_decoys)
    for i_decoy in range(num_decoys):
        e_decoy[i_decoy] = np.dot(gamma, phi_i_decoy[i_decoy])
    return e_decoy

def save_energy(e_decoy, filename):
    np.savetxt(filename, e_decoy, fmt='%f', delimiter='\n')

def main():
    gamma_file_name = 'gamma_10un1m'  
    phi_file_name = 'phi_10un1m_m'

    gamma = load_gamma(gamma_file_name)
    phi_i_decoy = load_phi(phi_file_name)
    e_decoy = calculate_energy(gamma, phi_i_decoy)
    save_energy(e_decoy, 'Energy_mg_10un1m_m.txt')

if __name__ == "__main__":
    main()
