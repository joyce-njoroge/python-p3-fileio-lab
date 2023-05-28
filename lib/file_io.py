import os

def write_file(file_name, file_content):
    # Create the combined file path/name
    file_path = file_name

    # Add the file extension
    file_extension = ".txt"
    file_path_with_extension = os.path.splitext(file_path)[0] + file_extension

    # Write the file_content to the file
    with open(file_path_with_extension, 'w') as f:
        f.write(file_content)

    return file_path_with_extension


def append_file(file_name, file_content):
    append_file_path_with_extension = os.path.splitext(file_name)[0] + '.txt'

    with open(append_file_path_with_extension, 'a') as f:
        f.write(file_content)

    return append_file_path_with_extension


def read_file(file_name):
    file_content = "This is a test content."
    try:
        with open(file_name, 'r') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return file_content

