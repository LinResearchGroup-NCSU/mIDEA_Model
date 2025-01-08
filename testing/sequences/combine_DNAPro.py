import re

def clean_and_combine(native_file, modeller_file, output_file):
    # Step 1: Read and clean the native sequence
    with open(native_file, 'r') as f:
        native_content = f.readline().strip()

    # Remove all non-uppercase characters (keep only A-Z)
    cleaned_native_content = re.sub(r'[^A-Z]', '', native_content)

    # Step 2: Read the modeller file line by line
    with open(modeller_file, 'r') as f:
        modeller_lines = f.readlines()

    # Step 3: Combine cleaned native sequence with each modeller line
    output_lines = [
        cleaned_native_content + line.strip() 
        for line in modeller_lines 
        if line.strip()  # Skip empty or whitespace-only lines
    ]

    # Step 4: Write the output to the output file
    with open(output_file, 'w') as out_f:
        out_f.write('\n'.join(output_lines) + '\n')  # Ensure a newline at the end of the file

# Example usage
clean_and_combine("native.seq", "dna_modeller.seq", "native.decoys")

