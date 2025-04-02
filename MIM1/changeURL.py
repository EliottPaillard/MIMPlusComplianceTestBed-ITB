import os
import sys

def replace_string_in_a_file(file_path, former_string, new_string):
        
    # Open the file and catch its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the former string with the new one
    modified_content = content.replace(former_string, new_string)

    # Open the file again and replace its content with the modified one
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
        
    # Print the name of the file    
    if modified_content != content :
        print(f"Modified file : {file_path}")

def browse_folder_and_replace(folder, former_string, new_string):
    
    # Browse recursively
    for root, subfolders, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml') or file.endswith('.json') or file.endswith('.jsonld') or file.endswith('.jsd'):
                file_path = os.path.join(root, file)
                replace_string_in_a_file(file_path, former_string, new_string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python changeURL.py <name_of_the_git_repository_owner>")
        sys.exit(1)

    new_string = sys.argv[1]

    browse_folder_and_replace(".", "herejusttobemodified", new_string)
