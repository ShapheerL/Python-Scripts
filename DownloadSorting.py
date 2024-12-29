import os
import shutil

def sortingDownloads(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        #Splicing the extension so its txt instead of .txt
        extension = os.path.splitext(file)[1][1:] 
        
        if not extension:  # Skip files without extensions
            continue
        
        folder_name = f"{extension} Files"
        destination_folder = os.path.join(folder_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)
        
        #source = f"{folder_path}\{file}"
        #destination = f"{folder_path}\{extension[1]}" Orignal Intention
        destination = os.path.join(destination_folder, file)
        shutil.move(file_path, destination)
        
sortingDownloads("C:/Users/narut/Downloads")