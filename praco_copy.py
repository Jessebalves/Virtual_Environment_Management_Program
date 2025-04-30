#import modules, consider adding more
import tkinter
import sys
import os
import shutil
import time

#initializing variables
files_local_directory = []
files_sub_directory = []
folders_local_directory = []
folders_sub_directory = []
thanks = "Thank you for checking out my program!"

#initlializing Graphical User Interface
window = tkinter.Tk()

menu = tkinter.Menu(window)
window.config(menu = menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label='HELP', menu = filemenu)
menu.add_command(label='ABOUT VEM', command=do_nothing)

#title of Graphical User Interface
window.title("VEM - Virtual Environment Management Program")
#size of Graphical User Interface
window.geometry("1920x1080")

text_widget = tkinter.Text(window,height =1920, width =1080,font = ("Times New Roman", 20))
text_widget.pack()

#function to exit program
def exit_program():
    #closes out of specified window(not working as intended)
    window.destroy()
    for value in thanks:
        print(value,end="")
        time.sleep(0.003)
    #exit program
    sys.exit(0)


#function that is associated with the tkinter buttons created
#still a work in progress
def clicked_button():
    print("Change directory test button")
    user_message3 = input("Which directory homie")
    os.chdir(user_message3)
    #window.destroy()
    

#Function to scan local folder
#appends findings to variables initialized in beginning of program
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

def scan_sub_files_and_folders():
    for value in folders_local_directory:
        previous_dir = os.getcwd()
        os.chdir(value)
        for items in os.listdir():
            if os.path.isfile(items):
                files_sub_directory.append(items)
            if os.path.isdir(items):
                folders_sub_directory.append(items)
        os.chdir(previous_dir)
        
#Deletes all the files and directories where this program is located
def delete_all_files():
    for item in os.listdir():
        if os.path.isfile(item) and item != "praco_copy.py":
            os.remove(item)
        if os.path.isdir(item):
            shutil.rmtree(item)
            
#figure out how to incorporate this function, using a button           
def delete_singular_file():
    delete_question = input("Which file would you like to delete? ")
    for item in os.listdir():
        if os.path.isfile(item) and item == delete_question:
            os.remove(item)
        elif os.path.isdir(item) and item == delete_question:
            shutil.rmtree(item)
        else:
            pass
        
    
#Function that deletes the program itself          
def delete_self():
    for file in files_local_directory:
        if file == "praco_copy.py":
            os.remove(file)    
                        
#print(OP_Message)          
OP_Message = ('Operating System on machine: ' + os.name)
Current_dir = ('\nCurrent working directory: ' + os.getcwd()+ '\n')

scan_for_files_and_folders()
#delete_singular_file(usr4)
scan_sub_files_and_folders()

#Print statements
print("Operating System on machine: ", os.name)
print("Operating System on machine: ", os.uname_result)
print("Operating System on machine: ", sys.platform)
print("Current working directory: ",os.getcwd(),"\n")
print("Folders found in Local Directories: ",folders_local_directory)
print("Folders found in Sub Directories: ", folders_sub_directory)
print("\n")
print("Files found in Main Directory: ",files_local_directory)
print("Files found in Sub Directory: ",files_sub_directory)
print("\n")

#more tkinter stuff, go through this and comment which each line does
text_widget.insert(tkinter.END,OP_Message)
Change_dir_button = tkinter.Button(window, text = "CHANGE DIRECTORY",command= clicked_button, font = ("Times New Roman", 18))
Change_dir_button.place(x=1000, y= 300)
Delete_single_button = tkinter.Button(window, text = "Delete Specific File", command = delete_singular_file, font = ("Times New Roman", 18))
Delete_single_button.place(x=1000,y=350)
Quit_button = tkinter.Button(window,text = "EXIT THE PROGRAM", command = exit_program,font = ("Times New Roman",18))
Quit_button.place(x=1000,y=400)
text_widget.insert(tkinter.END,Current_dir)
text_widget.insert(tkinter.END,"\n")
text_widget.insert(tkinter.END,'Folders found in Local Directories: ')
text_widget.insert(tkinter.END,folders_local_directory)
text_widget.insert(tkinter.END,'\nFolders found in Sub Directories: ')
text_widget.insert(tkinter.END,folders_sub_directory)
text_widget.insert(tkinter.END,"\n")
text_widget.insert(tkinter.END,"\nFiles found in Main Directory: ")
text_widget.insert(tkinter.END,files_local_directory)
text_widget.insert(tkinter.END,"\nFiles found in Sub Directory: ")
text_widget.insert(tkinter.END,files_sub_directory)
text_widget.insert(tkinter.END,"\n")
window.mainloop()
