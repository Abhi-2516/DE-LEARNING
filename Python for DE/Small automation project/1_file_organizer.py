"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

# we will use shutill

import os
import shutil

EXTENSION_TO_FOLDER = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
    "TextFiles": [".txt"],
    "Others": []  # Catch-all for other file types
}

def  get_destination_folder(filname):
    ext = os.path.splitext(filname)[1].lower() 
    # Get the file extension and convert to lowercase
    for folder, extensions in EXTENSION_TO_FOLDER.items()  :
        if ext in extensions:
            return folder
    return "Others"  # Default folder for unknown file types


def sort_files(source_folder):
    for files in os.listdir(source_folder):
        file_path = os.path.join(source_folder, files)
        if os.path.isfile(file_path):  
            destination_folder = get_destination_folder(files)
            destination_path = os.path.join(source_folder, destination_folder)
            os.makedirs(destination_path, exist_ok=True)  # Create folder if it doesn't exist
            shutil.move(file_path, os.path.join(destination_path, files))  # Move the file
   
            
if __name__ == "__main__":
    
    source_folder = input("Enter the folder path to organize (leave blank for current folder): ")
    if not source_folder:
        source_folder = os.getcwd()  # Use current working directory if no input
    sort_files(source_folder)
    print("Files have been organized.")
    
    

    
        

