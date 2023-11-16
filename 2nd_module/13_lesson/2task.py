import os
from typing import Optional, List


def gen_files_path(root_dir: str, target_dir: Optional[str] = ''):
    files_paths = []

    for root, _, files in os.walk(os.path.join(root_dir, target_dir)):
        for file in files:
            file_path = os.path.join(root, file)
            files_paths.append(file_path)

    return files_paths


root_directory = input("Enter the root directory: ")
target_directory = input("Enter the target directory: ")
files_list = gen_files_path(root_dir=root_directory, target_dir=target_directory)

for file_path in files_list:
    print(file_path)
