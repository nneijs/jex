import os
import sys

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def create_files(folder_name, num_files):
    for i in range(1, num_files + 1):
        file_name = f"{folder_name}_file_{i}.txt"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write(f"This is file {i} inside {folder_name}.")

        print(f"File '{file_name}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "add_jex":
        print("Please provide the command-line argument 'add_jex' to create folders and files.")
        sys.exit(1)

    folder_name = "jex_folder"
    num_files = 5  # You can change this to the desired number of files.

    create_folder(folder_name)
    create_files(folder_name, num_files)
