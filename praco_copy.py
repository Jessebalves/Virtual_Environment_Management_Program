import sys
import os
import shutil
import time


files_local_directory = []
files_sub_directory = []
folders_local_directory = []
folders_sub_directory = []
thanks = "Thank you for checking out my program!"

#only deletes files in main directory, not the sub directories
#subdirectory files are not being deleted
#if theres a folder within a folder, the folder is appended to the wrong list        

print("Operating System on machine: ", os.name)
print("Current working directory: ",os.getcwd(),"\n")

def scan_for_files_and_folders():
    try:
        for item in os.listdir():
            if os.path.isfile(item):
                files_local_directory.append(item)
            if os.path.isdir(item):
                folders_local_directory.append(item)
    except Exception as e:
        print(e)
    finally:
        return folders_local_directory and files_local_directory



#Deletes all the files and directories where this program is located
def delete_files():
    for item in os.listdir():
        if os.path.isfile(item) and item != "praco.py":
            os.remove(item)
        if os.path.isdir(item):
            shutil.rmtree(item)

#Function that deletes the program            
def delete_self():
    for file in files_local_directory:
        if file == "praco.py":
            os.remove(file)
                        
#Function that combines all the other functions together
def traverse():
    scan_for_files_and_folders()
    #delete_files()
    #delete_self()


traverse()

#sub directory for loops
for value in folders_local_directory:
    os.chdir(value)
    for items in os.listdir():
        if os.path.isfile(items):
            files_sub_directory.append(items)
        if os.path.isdir(items):
            folders_sub_directory.append(items)


#Print statements
print("Folders found in Local Directories: ",folders_local_directory)
print("Folders found in Sub Directories: ", folders_sub_directory)
print("\n")
print("Files found in Main Directory: ",files_local_directory)
print("Files found in Sub Directory: ",files_sub_directory)
print("\n")


user_message1 = input("Change Directory? (Enter yes or no)")
if user_message1 == "yes":
    user_message1 = input("What would you like to change the directory to?")
    print(os.getcwd())
elif user_message1 == "no":
    user_message2 = input("Would you like to exit the program?")
    if user_message2 == "yes":
        for value in thanks:
            print(value,end="")
            time.sleep(0.003)
        sys.exit(0)
    else:
        print("You gotta add code here bro... this a deadend")
else:
    print("sorry we dont quite understand")
    sys.exit(1)
