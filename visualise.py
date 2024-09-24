import sys
import os

# Update the path for Python 3
sys.path.append('/c5/shared/pymol/1.7.0.0-python-3.8.5-shared/lib/python3.8/site-packages/')

import __main__
__main__.pymol_argv = ['pymol', '-qc']  # Pymol: quiet and no GUI
import pymol
pymol.finish_launching()

# Check for the correct number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python3 visualise.py <path_to_pdb_file>")
    sys.exit(1)

# Load the PDB file
pdb_file = sys.argv[1]
if not os.path.isfile(pdb_file):
    print(f"Error: File '{pdb_file}' not found.")
    sys.exit(1)

# Use a safe filename
pdb_name = os.path.basename(pdb_file).split('.')[0]

# Load the PDB file into PyMOL
pymol.cmd.load(pdb_file, pdb_name)
pymol.cmd.disable("all")
pymol.cmd.enable(pdb_name)

# Print the names of the loaded objects
print(pymol.cmd.get_names())
pymol.cmd.hide('all')
pymol.cmd.show('cartoon')
pymol.cmd.set('ray_opaque_background', 0)
pymol.cmd.color('red', 'ss h')
pymol.cmd.color('yellow', 'ss s')

# Save the image
output_png = f"{pdb_name}.png"
pymol.cmd.png(output_png)  # Using f-string for formatting
print(f"Saved image as '{output_png}'")

# Quit PyMOL
pymol.cmd.quit()

