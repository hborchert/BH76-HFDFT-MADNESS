import os
import shutil
import pathlib

def copy_specific_file(input_dir, output_dir, filename):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through the input directory and its subdirectories
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Check if the file matches the specified filename
            if file == filename:
                # Create the corresponding directory structure in the output directory
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)

                # Construct the input and output file paths
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_subdir, file)

                # Copy the file to the output directory
                shutil.copy2(input_file_path, output_file_path)

# Define input and output directories
path = os.path.abspath(os.getcwd())
input_directory = path+'/hf/geometries'  # Change this to your desired input directory
output_directory = os.path.join(path, 'pbe')  # Change this to your desired output directorydirectory = os.path.join(path, 'hf')

print(input_directory, output_directory)

filename_to_copy = "struc.restartdata.00000"  # Replace with the specific filename to copy

copy_specific_file(input_directory, output_directory, filename_to_copy)