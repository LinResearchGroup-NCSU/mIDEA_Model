import re

def clean_and_combine(native_file, modeller_file, output_file):
    # Step 1: Read and clean the native sequence
    with open(native_file, 'r') as f:
        native_content = f.readline().strip()

    # Remove all non-uppercase characters (keep only A-Z)
    cleaned_native_content = re.sub(r'[^A-Z]', '', native_content)

    # Step 2: Process modeller file line by line and write directly to output
    with open(modeller_file, 'r') as modeller_f, open(output_file, 'w') as out_f:
        for line in modeller_f:
            modeller_line = line.strip()  # Remove whitespace from modeller line
            # Combine cleaned native sequence with the modeller line
            combined_line = cleaned_native_content + modeller_line
            out_f.write(combined_line + "\n")  # Write the result to output file

# Example usage
clean_and_combine("native.seq", "dna_modeller.seq", "native.decoys")
