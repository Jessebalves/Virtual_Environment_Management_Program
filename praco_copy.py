#import used for Graphical User Interface
import tkinter
from tkinter import ttk
#import used to exit system, close terminal upon exiting program
import sys
#main imports used to scan files/folders and remove them
import os
import shutil

#initializing global variables
#lists to store files
files_local_directory = []
files_sub_directory = []
folders_local_directory = []
folders_sub_directory = []
all_gui_windows = []

#function to exit program
#destroys all windows open
#Example: the master window and help window are open, this function will close both
def destroy_all_windows():
    for value in all_gui_windows:
        value.destroy()
    window.destroy()
    #exit program
    sys.exit(0)
    
#function that is associated with the tkinter buttons created
#still a work in progress
def clicked_button():
    print("Change directory test button")
    user_message3 = input("Which directory homie")
    os.chdir(user_message3)


#Function to scan local folder
#appends findings to variables initialized in beginning of program
def scan_for_files_and_folders():
    try:
        for item in os.listdir():
            if os.path.isfile(item) and item != ".DS_Store":
                files_local_directory.append(item)
            if os.path.isdir(item):
                folders_local_directory.append(item)
    except Exception as e:
        print(e)
    finally:
        return folders_local_directory and files_local_directory

#this function is dependent on folders and files locally being returned
#function used to scan sub directories
def scan_sub_files_and_folders():
    for value in folders_local_directory:
        previous_dir = os.getcwd()
        os.chdir(value)
        for items in os.listdir():
            if os.path.isfile(items) and items != ".DS_Store":
                files_sub_directory.append(items)
            if os.path.isdir(items):
                folders_sub_directory.append(items)
        os.chdir(previous_dir)
        
#Deletes all the files where this program is located
def delete_all_files():
    for item in os.listdir():
        if os.path.isfile(item) and item != "praco_copy.py":
            os.remove(item)
            
#Deletes all folders in directory program is located            
def delete_all_folders():
    for item in os.listdir():
        if os.path.isdir(item):
            shutil.rmtree(item)
            
#figure out how to incorporate this function, using a button           
def delete_singular_file():
    delete_question = input("Which file would you like to delete? ")
    for item in os.listdir():
        if os.path.isfile(item) and item == delete_question:
            os.remove(item)
        else:
            pass

#function designed to delete a single folder
def delete_singular_folder():
    delete_question1 = input("Which folder would you like to delete?")
    for item in os.listdir():
        if os.path.isdir(item) and item == delete_question1:
            shutil.rmtree(item)
        else:
            pass
        
#Function that deletes the program itself          
def delete_self():
    for file in files_local_directory:
        if file == "praco_copy.py":
            os.remove(file)
            
#function associated with help menu About VEM
#creates another Graphical User Interface containing help documentation         
def help_gui():
    root = tkinter.Tk()
    all_gui_windows.append(root)
    root.title('VEM - HELP')
    root.geometry("1920x1080")
    #Initilazing textbox. Specifies which gui, size of text_widget we put on GUI, and size of font that is inserted to widget
    text_widget_2 = tkinter.Text(root,height = "1920", width = "1080",font = ("Times New Roman",16),background= "lightyellow")
    text_widget_2.insert(tkinter.END, "This program was created to manage files and folders/directories")
    text_widget_2.insert(tkinter.END, " on a computer within a GUI (Graphical User Interface).\n")
    text_widget_2.insert(tkinter.END, "This program scans folders and files within a directory it is ran in.")
    text_widget_2.insert(tkinter.END, "This program provides users with many options to navigate the file system.\n")
    text_widget_2.insert(tkinter.END, "This program acts as a file explorer within a Python Graphical User Interface.\n")
    text_widget_2.insert(tkinter.END, "\nFile - a resource in computing where you can store, record, and manipulate information. There are very many different types with different file extensions.\n")
    text_widget_2.insert(tkinter.END, "\nFolder - a special type of file that contains files and other folders.\n")
    text_widget_2.insert(tkinter.END, "\nDirectory - Is the same as a folder however slightly different. Directory refers to location in the file system of your machine.")
    text_widget_2.insert(tkinter.END, "\nExample of a directory: /Users/YourName/Desktop/Random_Folder/\n")
    text_widget_2.insert(tkinter.END, "\nCWD - Stands for current working directory. This means the directory we currently")
    text_widget_2.insert(tkinter.END, " are working in/currently looking at.\n")
    text_widget_2.insert(tkinter.END, "KEEP IN MIND - You can only delete files/folders in the current working directory.\n\n")
    text_widget_2.insert(tkinter.END, "This program also focuses on OS(Operating Systems), and the OS import.\n")
    text_widget_2.insert(tkinter.END, "Operating System - Most important software component on a computer. Acts as an interface between hardware and the user.")
    text_widget_2.insert(tkinter.END, "\nOperating Systems are responsible for managing tasks, managing memory, and managing files.\n")
    text_widget_2.insert(tkinter.END, "\nThis program can display differently depending upon what operating system")
    text_widget_2.insert(tkinter.END, " your machine uses.\nThese are the operating systems present on the machines")
    text_widget_2.insert(tkinter.END, " used to develop this software.\n")
    text_widget_2.insert(tkinter.END, "nt - Windows nt\n")
    text_widget_2.insert(tkinter.END, "posix - Mac OS High Sierra\n")
    text_widget_2.insert(tkinter.END, "\nButton Commands Explanation:\nOpen File - Open a specified file\n")
    text_widget_2.insert(tkinter.END, "Copy File - Copy specified file to specified directory\n")
    text_widget_2.insert(tkinter.END, "Change Directory - Change directory being currently looked at\n")
    text_widget_2.insert(tkinter.END, "Delete Options - Able to delete singular items, or all items at once")
    text_widget_2.insert(tkinter.END, ". Items in this case refer to files or folders\n")
    text_widget_2.insert(tkinter.END, "Exit Program - Forcefully closes all windows and script\n")
    text_widget_2.insert(tkinter.END, "\nFor additional help, email Jessebalves@gmail.com.")
    
    #Actually placing the widget onto the GUI
    text_widget_2.pack()

#initlializing Graphical User Interface
window = tkinter.Tk()

#title of Graphical User Interface
window.title("VEM - Virtual Environment Management Program")

#styles the buttons
style = ttk.Style(window)
style.theme_use('classic')

#photo that will be used as icon, must be present in directory
icon_photo = tkinter.PhotoImage(file = 'cleanerrr.png') 
  
# Setting icon of master window, this icon appears on task bar
window.iconphoto(False, icon_photo)

#size of Graphical User Interface
window.geometry("1920x1080")

#Initilazing textbox. Specifies which gui, size of text_widget we put on GUI, and size of font that is inserted to widget
text_widget = tkinter.Text(window,height =1920, width =1080,font = ("Open Sans", 25), background= "lightyellow")

#Actually placing the widget onto the GUI
text_widget.pack()

                  
#print(OP_Message)          
OP_Message = ('Operating System on machine: ' + os.name)
Current_dir = ('\nCurrent working directory: ' + os.getcwd()+ '\n')

#calling functions
scan_for_files_and_folders()
scan_sub_files_and_folders()

#Print statements
"""print("Operating System on machine: ", os.name)
print("Operating System on machine: ", os.uname_result)
print("Operating System on machine: ", sys.platform)
print("Current working directory: ",os.getcwd(),"\n")
print("Folders found in Local Directories: ",folders_local_directory)
print("Folders found in Sub Directories: ", folders_sub_directory)
print("\n")
print("Files found in Main Directory: ",files_local_directory)
print("Files found in Sub Directory: ",files_sub_directory)
print("\n")"""

#more tkinter stuff, go through this and comment which each line does
menu = tkinter.Menu(window)
window.config(menu = menu)
filemenu = tkinter.Menu(menu,tearoff=0)
menu.add_cascade(label='Help',menu=filemenu)
filemenu.add_command(label='ABOUT VEM',command = help_gui, accelerator = "CTRL-Z")
filemenu.add_separator()
filemenu.add_command(label='EXIT', command = destroy_all_windows, accelerator = "CTRL-Q")

#Graphical User Interface, text_widget
text_widget.tag_configure("center", justify='center')
text_widget.insert("1.0", "Welcome to VEM!")
text_widget.tag_add("center", "1.0", "end")
text_widget.insert(tkinter.END, "\n")
text_widget.insert(tkinter.END,"\n")
text_widget.insert(tkinter.END,OP_Message)

#Buttons for GUI
#change directory button
Change_dir_button = tkinter.Button(window, text = "CHANGE DIRECTORY",command= clicked_button, font = ("Times New Roman", 18))
Change_dir_button.place(x=850, y= 400)

#delete single folder button
Delete_single_folder = tkinter.Button(window, text = "DELETE SINGLE FOLDER", command = delete_singular_folder, font = ("Times New Roman", 18))
Delete_single_folder.place(x = 850, y = 450)

#delete single file button
Delete_single_button = tkinter.Button(window, text = "DELETE SINGLE FILE", command = delete_singular_file, font = ("Times New Roman", 18))
Delete_single_button.place(x=850,y=500)

#Delete all files in current working directory
Delete_all_files_cwd = tkinter.Button(window, text = "DELETE ALL FILES (CWD)", command = delete_all_files, font = ("Times New Roman", 18))
Delete_all_files_cwd.place(x = 850, y =550)

#delete all folders in current working directory
Delete_all_folders_cwd = tkinter.Button(window, text = "DELETE ALL FOLDERS(CWD)", command = delete_all_folders, font = ("Times New Roman", 18))
Delete_all_folders_cwd.place(x = 850, y = 600)
        
#exit program button, just closes the window and exits the program
Quit_button = tkinter.Button(window,text = "EXIT THE PROGRAM", command = destroy_all_windows,font = ("Times New Roman",18))
Quit_button.place(x=850,y=650)

#More text_widget insertions
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
