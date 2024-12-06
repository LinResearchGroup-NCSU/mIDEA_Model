def replace_and_generate_file(native_file, modeller_file, output_file):
    import re

    # Read and clean the native sequence (remove non-uppercase characters)
    with open(native_file, 'r') as f:
        native_content = f.readline().strip()
    filtered_native_content = re.sub(r'[^A-Z]', '', native_content)

    # Read modeller lines
    with open(modeller_file, 'r') as f:
        modeller_lines = f.readlines()

    # Write the cleaned content with modeller sequences
    with open(output_file, 'w') as out_f:
        for modeller_line in modeller_lines:
            modeller_line = modeller_line.strip()
            # Replace each modeller line directly in place of the cleaned sequence
            out_f.write(filtered_native_content + modeller_line + "\n")


replace_and_generate_file("native.seq", "dna_modeller.seq", "native.decoys")
