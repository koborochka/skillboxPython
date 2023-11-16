import os

def count_lines_in_python_files(directory: str):

    if not os.path.exists(directory):
        print("Directory not found.")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_name = os.path.relpath(file_path, directory)

                with open(file_path, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

                yield file_name, len(lines)

directory_path = input("Enter the target directory path: ")
for file_name, lines_count in count_lines_in_python_files(directory_path):
    print(f"File: {file_name}, Lines Count: {lines_count}")
