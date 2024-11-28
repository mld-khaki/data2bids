import os
import re
import sys

def generate_pipeline(input_folder=None):
    try:
        # Step 1: If input_folder is not provided, check for command-line argument
        if input_folder is None:
            if len(sys.argv) > 1:  # Check if a command-line argument is provided
                input_folder = sys.argv[1]
            else:  # Prompt the user for a folder path or use the current working directory
                input_folder = input("Enter the folder path to process, or press Enter to use the current folder: ").strip()
                if not input_folder:
                    input_folder = os.getcwd()

        # Normalize the input folder path to handle relative paths and ensure consistency
        input_folder = os.path.abspath(input_folder)

        # Step 2: Validate the input folder
        if not os.path.exists(input_folder):  # Check if the folder exists
            raise FileNotFoundError(f"The folder '{input_folder}' does not exist.")
        if not os.path.isdir(input_folder):  # Ensure the path is a directory
            raise NotADirectoryError(f"The path '{input_folder}' is not a directory.")

        # Step 3: Check for files in the folder
        contents = os.listdir(input_folder)  # List all items in the folder
        if any(os.path.isfile(os.path.join(input_folder, item)) for item in contents):
            # Raise an error if the folder contains any files
            raise ValueError(f"The folder '{input_folder}' contains files. Only folders are allowed.")

        # Step 4: Define folder naming pattern
        # Regex to match folder names in the specified format, allowing spaces and following UUID conventions
        folder_pattern = re.compile(
            r"^[\w\s]+~[\w\s]+_[\da-fA-F]{8}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{12}$"
        )

        # Step 5: Generate pipeline
        output_lines = []  # List to store pipeline output lines
        for folder_name in contents:
            folder_path = os.path.join(input_folder, folder_name)
            # Check if the item is a directory and matches the naming pattern
            if os.path.isdir(folder_path) and folder_pattern.match(folder_name):
                eeg_file = os.path.join(folder_path, f"{folder_name}.eeg")  # Expected EEG file
                if not os.path.exists(eeg_file):  # Ensure the .eeg file exists
                    raise FileNotFoundError(f"The expected EEG file '{eeg_file}' does not exist.")
                # Format the output line
                output_line = f"{folder_path}\\{folder_name}.eeg, D:\\Neuroworks\\Settings\\quantum_new.exp"
                output_lines.append(output_line)

        # Raise an error if no valid folders are found
        if not output_lines:
            raise ValueError(f"No valid folders matching the naming pattern were found in '{input_folder}'.")

        # Step 6: Write the output to a file
        output_file = os.path.join(input_folder, "pipeline_output.txt")
        with open(output_file, "w") as f:
            f.write("\n".join(output_lines))  # Write all output lines to the file
        
        print(f"Pipeline file successfully created: {output_file}")

    except Exception as e:
        # Handle any exceptions and provide detailed error messages
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    generate_pipeline()
