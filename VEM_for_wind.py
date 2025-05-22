#import used for Graphical User Interface
import tkinter
from tkinter import ttk
from tkinter import messagebox
#import used to exit system, close terminal upon exiting program
import sys
#main imports used to scan files/folders and remove them
import os
import shutil
#used for open file
import subprocess

#initializing global variables
#lists to store files
files_local_directory = []
files_sub_directory = []
folders_local_directory = []
folders_sub_directory = []
all_gui_windows = []
#we need to use directory location for this variable
#this is because we can constantly change directories
icon_photo_location = (os.getcwd() + "/cleanerrr.png")

#function associated with initial scan of CWD
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
#function used to scan sub directories(in other words, folders attached to CWD)
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

#section of code signifying the start of the program
#initial scan for data before populating GUI
print("VEM starting...")
print("Beginning initial scan of directories")
scan_for_files_and_folders()
scan_sub_files_and_folders()

#main function to create a GUI
def generate_gui():
    #function to exit program
    #destroys all windows open
    #Example: the master window and help window are open, this function will close both
    def destroy_all_windows():
        for value in all_gui_windows:
            value.destroy()
        #closes GUIS
        window.destroy()
        #exit program, closes terminal
        print("Closing VEM...")
        sys.exit(0)
        
    #Function associated with Change Directory button
    def change_directory_button():
        def cancel():
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            user_message3 = entry.get()
            if os.path.exists(user_message3) == True:
                print("This directory does exist")
                
                os.chdir(user_message3)
                window.destroy()
                

                for item in files_sub_directory:
                    files_sub_directory.remove(item)
                    files_sub_directory.clear()
                    
                for item in folders_local_directory:
                    folders_local_directory.remove(item)
                    folders_local_directory.clear()
                    
                for item in folders_sub_directory:
                    folders_sub_directory.remove(item)
                    folders_sub_directory.clear()
                    
                for items in files_local_directory:
                    files_local_directory.remove(items)
                    files_local_directory.clear()


                print(files_sub_directory)
                print(folders_local_directory)
                print(folders_sub_directory)
                print(files_local_directory)

                scan_for_files_and_folders()
                scan_sub_files_and_folders()
                generate_gui()
                
            else:
                print("This directory does not exist")
    
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
                        
        #user input within graphical user interface
        entry = tkinter.Entry(window, width=25)
        entry.pack()
        entry.insert(0,"directory name")
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",width = 20, command=get_input)
        button_test.pack()

        cancel_button = tkinter.Button(window,text="Cancel",width = 20, command=cancel)
        cancel_button.pack()
            

            
    #Deletes all the files where this program is located
    def delete_all_files():
        questo = messagebox.askquestion("ALERT!", "Are you sure you want to delete all files in Current working directory?")
        if questo == "yes":
            for item in os.listdir():
                if os.path.isfile(item):
                    if item =="VEM_for_mac.py" or item =="cleanerrr.png":
                         pass
                    else:  
                        os.remove(item)
                        files_local_directory.remove(item)
            window.destroy()
            generate_gui()
        else:
            pass

    #Deletes all folders in directory program is located            
    def delete_all_folders():
        warning_box = messagebox.askquestion("ALERT!", "Are you sure you want to delete all folders in Current working directory?")
        if warning_box == "yes":
            for item in os.listdir():
                if os.path.isdir(item):
                    shutil.rmtree(item)
                    folders_local_directory.remove(item)
            window.destroy()
            generate_gui()
        else:
            pass
        
                
    #figure out how to incorporate this function, using a button           
    def delete_singular_file():
        def cancel():
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            delete_question = entry.get()
            for item in os.listdir():
                if os.path.isfile(item) and item == delete_question:
                    os.remove(item)
                    files_local_directory.remove(item)
                else:
                    pass
                
            #we destroy window and generate gui
            #we do this to "refresh" the GUI
            #to properly display new data in file system
            window.destroy()
            generate_gui()

            #after deleting the specified file, destroy text box and buttons
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
                        
        #user input within graphical user interface
        entry = tkinter.Entry(window, width=25)
        entry.pack()
        
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",width = 20,command=get_input)
        button_test.pack()

        #cancel button placement and initialization
        cancel_button = tkinter.Button(window,text="Cancel",width = 20,command=cancel)
        cancel_button.pack()

    #function designed to delete a single folder
    def delete_singular_folder():
        def cancel():
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            delete_question1 = entry.get()
            for item in os.listdir():
                if os.path.isdir(item) and item == delete_question1:
                    shutil.rmtree(item)
                    folders_local_directory.remove(item)
                else:
                    pass
            #we destroy window and generate gui
            #we do this to "refresh" the GUI
            #to properly display new data in file system
            window.destroy()
            generate_gui()

            
        #user input within graphical user interface
        entry = tkinter.Entry(window, width=25)
        entry.pack()
        
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",width = 20,command=get_input)
        button_test.pack()

        #cancel button placement and initialization
        cancel_button = tkinter.Button(window,text="Cancel",width = 20,command=cancel)
        cancel_button.pack()
                
    #function associated with help menu About VEM
    #creates another Graphical User Interface containing help documentation         
    def help_gui():
        root = tkinter.Tk()
        all_gui_windows.append(root)
        root.title('VEM - HELP')
        root.geometry("640x480")
        #Initilazing textbox. Specifies which gui, size of text_widget we put on GUI, and size of font that is inserted to widget
        text_widget_2 = tkinter.Text(root,height = "640", width = "480",font = ("Times New Roman",12),background= "lightyellow")
        text_widget_2.insert(tkinter.END, "This program was created to manage files and folders/directories")
        text_widget_2.insert(tkinter.END, " on a computer within a GUI (Graphical User Interface).\n")
        text_widget_2.insert(tkinter.END, "This program scans folders and files within a directory it is ran in.")
        text_widget_2.insert(tkinter.END, "This program provides users with many options to navigate the file system. Each button has their own function.\n")
        text_widget_2.insert(tkinter.END, "Some of the buttons prompt user input through the interface, other buttons have caution message boxes appear ensuring no accidental deletion.\n")
        text_widget_2.insert(tkinter.END, "This program acts as a file explorer within a Python Graphical User Interface.\n")
        text_widget_2.insert(tkinter.END, "\nFile \t\t\t- a resource in computing where you can store, record, and manipulate \n\t\t\tinformation. There are very many different types with different file extensions.\n")
        text_widget_2.insert(tkinter.END, "\nFolder \t\t\t- a special type of file that contains files and other folders.\n")
        text_widget_2.insert(tkinter.END, "\nDirectory \t\t\t- Is the same as a folder however slightly different. Directory refers to \n\t\t\tlocation in the file system of your machine.")
        text_widget_2.insert(tkinter.END, "\nExample of a directory \t\t\t- /Users/YourName/Desktop/Random_Folder/\n")
        text_widget_2.insert(tkinter.END, "\nCWD \t\t\t- Stands for current working directory. This means the directory we currently")
        text_widget_2.insert(tkinter.END, " are working \n\t\t\tin/currently looking at.\n")
        text_widget_2.insert(tkinter.END, "KEEP IN MIND \t\t\t- You can only delete files/folders in the current working directory.\n\n")
        text_widget_2.insert(tkinter.END, "This program also focuses on OS(Operating Systems), and the OS import.\n")
        text_widget_2.insert(tkinter.END, "Operating Systems are responsible for managing tasks, managing memory, and managing files.\n")
        text_widget_2.insert(tkinter.END, "Operating System \t\t\t- Most important software component on a computer. Acts as an \n\t\t\tinterface between hardware and the user.\n")
        text_widget_2.insert(tkinter.END, "\nThis program can display differently depending upon what operating system")
        text_widget_2.insert(tkinter.END, " your machine uses.\nThese are the operating systems present on the machines")
        text_widget_2.insert(tkinter.END, " used to develop this software.\n")
        text_widget_2.insert(tkinter.END, "nt \t\t\t- Windows nt\n")
        text_widget_2.insert(tkinter.END, "posix \t\t\t- Mac OS High Sierra\n")
        text_widget_2.insert(tkinter.END, "\nButton Commands Explanation:\nOpen File \t\t\t- Open a specified file within the main directory\n")
        text_widget_2.insert(tkinter.END, "Copy File \t\t\t- Copy specified file to main directory\n")
        text_widget_2.insert(tkinter.END, "Copy Folder \t\t\t- Copy specified folder to current working directory\n")
        text_widget_2.insert(tkinter.END, "Change Directory \t\t\t- Change directory being currently looked at\n")
        text_widget_2.insert(tkinter.END, "Delete Options \t\t\t- Able to delete singular items, or all items at once")
        text_widget_2.insert(tkinter.END, ". Items in this case refer to files or folders\n")
        text_widget_2.insert(tkinter.END, "Exit Program \t\t\t- Forcefully closes all windows and script\n")
        text_widget_2.insert(tkinter.END, "\nFor additional help, email Jessebalves@gmail.com.")
        text_widget_2.insert(tkinter.END, "\nCopyright (c) 2024-2025 Jesse B. Alves Coding\n")
        text_widget_2.insert(tkinter.END, "All Rights Reserved.\n\n")
        text_widget_2.insert(tkinter.END, sys.copyright)
        
        #Actually placing the widget onto the GUI
        text_widget_2.pack()

        #if this window is closed, remove it from the list since it has already been closed
        if root.destroy:
            all_gui_windows.remove(root)


    #Function associated with pressing the open file button
    def Open_File_Button():
        def cancel():
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            user_input = entry.get()
            for item in os.listdir():
                if os.path.isfile(item) and item == user_input :
                    #Mac OS specific code
                    if sys.platform == "darwin":
                        opener = "open"
                    #Windows 10 specific code
                    elif sys.platform == "win32":
                        os.startfile(item)
                        entry.destroy()
                        button_test.destroy()
                    else:
                        opener = "xdg-open"
                    #Mac Os specific code
                    if sys.platform == "darwin":
                        subprocess.call([opener,item])
            entry.destroy()
            button_test.destroy()
            cancel_button.destroy()
                        
        #user input within graphical user interface
        entry = tkinter.Entry(window, width=25)
        entry.pack()
        entry.insert(0,"file_name.file_type")
        
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit", width = 20, command=get_input)
        button_test.pack()

        cancel_button = tkinter.Button(window,text="Cancel", width = 20, command=cancel)
        cancel_button.pack()

    #Function associated with pressing the Copy File Button
    def Copy_File_Button():
        def cancel():
            entry.destroy()
            entry2.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            user_input = entry.get()
            user_input1 = entry2.get()
        
            #copy_file_user_input = input("Which file would you like to copy?")
            #copied_name = input("What would you like to name the copied file?")
            shutil.copy(user_input,user_input1)
            entry.destroy()
            entry2.destroy()
            button_test.destroy()
            cancel_button.destroy()
            
        entry = tkinter.Entry(window, width=25)
        entry.insert(0,'File_name')
        
        entry2 = tkinter.Entry(window,width=25)
        entry2.insert(0,'Copied_file_name')

        entry.pack()
        entry2.pack()
        
        button_test = tkinter.Button(window, text = "Submit", width = 20, command=get_input)
        button_test.pack()

        cancel_button = tkinter.Button(window,text="Cancel", width = 20, command=cancel)
        cancel_button.pack()
        

    #Function associated with Copy Folder Button on Graphical User Interface
    def Copy_Folder_Button():
        def cancel():
            entry.destroy()
            entry2.destroy()
            button_test.destroy()
            cancel_button.destroy()
        def get_input():
            user_input = entry.get()
            user_input1 = entry2.get()
            
            #copy_folder_user_input = input("Which folder would you like to copy?")
            #copy_folder_name = input("Name the copied folder: ")
            shutil.copytree(user_input,user_input1)

            #test for refreshing GUI
            folders_local_directory.append(user_input1)
            window.destroy()
            generate_gui()
            
            entry.destroy()
            entry2.destroy()
            button_test.destroy()
            cancel_button.destroy()

        entry = tkinter.Entry(window, width=25)
        entry.insert(0,'Folder name')
        
        entry2 = tkinter.Entry(window,width=25)
        entry2.insert(0,'Copied_folder_name')
        
        entry.pack()
        entry2.pack()
        
        button_test = tkinter.Button(window, text = "Submit",width = 20,command=get_input)
        button_test.pack()

        cancel_button = tkinter.Button(window,text="Cancel",width = 20,command=cancel)
        cancel_button.pack()

    #initlializing Graphical User Interface
    window = tkinter.Tk()    

    #title of Graphical User Interface
    window.title("VEM - Virtual Environment Management Program")

    #styles the buttons
    style = ttk.Style(window)
    style.theme_use('classic')

    #exception handling that deals with the condition that the program's
    #icon photo cannot be located within the file system
    try:
        #photo that will be used as icon, must be present in directory
        icon_photo = tkinter.PhotoImage(file = icon_photo_location)
      
        # Setting icon of master window, this icon appears on task bar
        window.iconphoto(False, icon_photo)
    except tkinter.TclError as e:
        print("There was an error loading the icon photo")
        print("Make sure VEM is initally ran in the same folder as icon photo")

    #size of Graphical User Interface
    window.geometry("880x640")
    window.configure(bg = "white")
                      
    #print(OP_Message)          
    OP_Message = ('Operating System on Machine: ' + os.name)
    Current_dir = ('\nCurrent Working Directory: ' + os.getcwd()+ '\n')

    #Print statements
    print("\nStarting to pack GUI with the following data: ")
    print("Operating System on machine: ", os.name)
    print("Operating System on machine: ", os.uname_result)
    print("Operating System on machine: ", sys.platform)
    print("Current working directory: ",os.getcwd(),"\n")
    print("Folders found in Local Directories: ",folders_local_directory)
    print("Folders found in Sub Directories: ", folders_sub_directory)
    print("\n")
    print("Files found in Main Directory: ",files_local_directory)
    print("Files found in Sub Directory: ",files_sub_directory)

    #more tkinter stuff, go through this and comment which each line does
    menu = tkinter.Menu(window, bg = "white")
    window.config(menu = menu)
    filemenu = tkinter.Menu(menu,tearoff=0)
    menu.add_cascade(label='Help',menu=filemenu)
    filemenu.add_command(label='ABOUT VEM',command = help_gui, accelerator = "CTRL-Z")
    filemenu.add_separator()
    filemenu.add_command(label='EXIT', command = destroy_all_windows, accelerator = "CTRL-Q")

    Files_found_in_cwd = ("\nFiles found in Current Working Directory: [ ")
    Folders_found_in_cwd = ("\n\nFolders found in Current Working Directory: [ ")

    Files_found_in_sub = ("\n\nFiles found in Sub Directories: [ ")
    Folders_found_in_sub = ("\n\nFolders found in Sub Directories: [ ")
    
    
    for value in files_local_directory:
        if value != files_local_directory[-1]:
            Files_found_in_cwd += ("'" + value +"', ")
        else:
            Files_found_in_cwd += ("'" + value + "' ]")
    if not files_local_directory:
        Files_found_in_cwd +="]"
    
    for value in folders_local_directory:
        if value != folders_local_directory[-1]:
            Folders_found_in_cwd += ("'" + value +"', ")
        else:
            Folders_found_in_cwd += ("'" + value + "' ]")
    if not folders_local_directory:
        Folders_found_in_cwd += "]"
        
    for value in folders_sub_directory:
        if value != folders_sub_directory[-1]:
            Folders_found_in_sub += ("'" + value +"', ")
        else:
            Folders_found_in_sub += ("'" + value +"' ]")
    if not folders_sub_directory:
        Folders_found_in_sub += "]"

    for value in files_sub_directory:
        if value != files_sub_directory[-1]:
            Files_found_in_sub += ("'" + value +"', ")
        elif value == files_sub_directory[-1]:
            Files_found_in_sub += ("'" + value+"' ]")
    if not files_sub_directory:
        Files_found_in_sub += "]"

    label = tkinter.Label(window,wraplength=880, bg = "white", text = "Welcome to VEM!\n\n"+
                          OP_Message+
                          Current_dir+
                          Files_found_in_cwd+
                          Folders_found_in_cwd+
                          Files_found_in_sub+
                          Folders_found_in_sub)

    label.pack()

    
    #Buttons For GUI
    #Open File Button
    Open_File_Button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "OPEN FILE", command = Open_File_Button, font = ("Times New Roman", 12))
    Open_File_Button1.pack()

    #Copy File Button
    Copy_File_Button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "COPY FILE", command = Copy_File_Button, font = ("Times New Roman", 12))
    Copy_File_Button1.pack()

    #Copy Folder Button
    Copy_Folder_Button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "COPY FOLDER", command = Copy_Folder_Button, font = ("Times New Roman", 12))
    Copy_Folder_Button1.pack()

    #Change Directory Button
    Change_dir_button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "CHANGE DIRECTORY",command = change_directory_button, font = ("Times New Roman", 12))
    Change_dir_button1.pack()

    #Delete Single Folder Button
    Delete_single_folder1 = tkinter.Button(window, height= -5, width = 25, bg = "lightblue", text = "DELETE SINGLE FOLDER", command = delete_singular_folder, font = ("Times New Roman", 12))
    Delete_single_folder1.pack()

    #Delete Single File Button
    Delete_single_button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "DELETE SINGLE FILE", command = delete_singular_file, font = ("Times New Roman", 12))
    Delete_single_button1.pack()

    #Delete all files in current working directory
    Delete_all_files_cwd1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "DELETE ALL FILES (CWD)", command = delete_all_files, font = ("Times New Roman", 12))
    Delete_all_files_cwd1.pack()

    #delete all folders in current working directory
    Delete_all_folders_cwd1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "DELETE ALL FOLDERS(CWD)", command = delete_all_folders, font = ("Times New Roman", 12))
    Delete_all_folders_cwd1.pack()
                
    #exit program button, just closes the window and exits the program
    Quit_button1 = tkinter.Button(window, height= -5, width=25, bg = "lightblue", text = "EXIT THE PROGRAM", command = destroy_all_windows,font = ("Times New Roman",12))
    Quit_button1.pack()

    #running the window
    window.mainloop()

#main method 
if __name__ == '__main__':
    generate_gui()
