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

scan_for_files_and_folders()
scan_sub_files_and_folders()

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
        sys.exit(0)
        
    #function that is associated with the tkinter buttons created
    #still a work in progress
    def change_directory_button():
        print("Change directory test button")
        user_message3 = input("Which directory homie")
        if os.path.exists(user_message3) == True:
            print("This directory does exist")
            os.chdir(user_message3)
            window.destroy()

            for item in files_sub_directory:
                files_sub_directory.remove(item)
            for item in folders_local_directory:
                folders_local_directory.remove(item)
            for item in folders_sub_directory:
                folders_sub_directory.remove(item)
            for items in files_local_directory:
                files_local_directory.remove(items)
            #for some reason, after the first for loop
            #one file will still be present in the list
            #this second for loop ensures removal of the
            #singular item from the list
            for item in files_local_directory:
                files_local_directory.remove(item)

            scan_for_files_and_folders()
            scan_sub_files_and_folders()
            generate_gui()
            
        else:
            print("This directory does not exist")
            

            
    #Deletes all the files where this program is located
    def delete_all_files():
        questo = messagebox.askquestion("ALERT!", "Are you sure you want to delete all files in Current working directory?")
        if questo == "yes":
            for item in os.listdir():
                if os.path.isfile(item):
                    if item =="pracoooo.py" or item =="cleanerrr.png":
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
        entry = tkinter.Entry(window, width=30)
        entry.place(relx=0.55,rely=0.45,anchor=tkinter.CENTER)
        
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",command=get_input)
        button_test.place(relx=0.57, rely = 0.45)

        #cancel button placement and initialization
        cancel_button = tkinter.Button(window,text="Cancel",command=cancel)
        cancel_button.place(relx = 0.59, rely = 0.45)

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
        entry = tkinter.Entry(window, width=30)
        entry.place(relx=0.55,rely=0.45,anchor=tkinter.CENTER)
        
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",command=get_input)
        button_test.place(relx=0.57, rely = 0.45)

        #cancel button placement and initialization
        cancel_button = tkinter.Button(window,text="Cancel",command=cancel)
        cancel_button.place(relx = 0.59, rely = 0.45)
                
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
        text_widget_2.insert(tkinter.END, "This program provides users with many options to navigate the file system. Each button has their own function.\n")
        text_widget_2.insert(tkinter.END, "Some of the buttons prompt user input through the interface, other buttons have caution message boxes appear ensuring no accidental deletion.\n")
        text_widget_2.insert(tkinter.END, "This program acts as a file explorer within a Python Graphical User Interface.\n")
        text_widget_2.insert(tkinter.END, "\nFile \t\t\t- a resource in computing where you can store, record, and manipulate information. There are very many different types with different file extensions.\n")
        text_widget_2.insert(tkinter.END, "\nFolder \t\t\t- a special type of file that contains files and other folders.\n")
        text_widget_2.insert(tkinter.END, "\nDirectory \t\t\t- Is the same as a folder however slightly different. Directory refers to location in the file system of your machine.")
        text_widget_2.insert(tkinter.END, "\nExample of a directory \t\t\t- /Users/YourName/Desktop/Random_Folder/\n")
        text_widget_2.insert(tkinter.END, "\nCWD \t\t\t- Stands for current working directory. This means the directory we currently")
        text_widget_2.insert(tkinter.END, " are working in/currently looking at.\n")
        text_widget_2.insert(tkinter.END, "KEEP IN MIND \t\t\t- You can only delete files/folders in the current working directory.\n\n")
        text_widget_2.insert(tkinter.END, "This program also focuses on OS(Operating Systems), and the OS import.\n")
        text_widget_2.insert(tkinter.END, "Operating Systems are responsible for managing tasks, managing memory, and managing files.\n")
        text_widget_2.insert(tkinter.END, "Operating System \t\t\t- Most important software component on a computer. Acts as an interface between hardware and the user.\n")
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

    #model for getting input from entries
    def get_input():
       user_input = entry.get()
       print(user_input)

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
        entry = tkinter.Entry(window, width=30)
        entry.place(relx=0.65,rely=0.45,anchor=tkinter.CENTER)
        #button associated with getting the user input
        button_test = tkinter.Button(window, text = "Submit",command=get_input)
        button_test.place(relx=0.8, rely = 0.43)

        cancel_button = tkinter.Button(window,text="Cancel",command=cancel)
        cancel_button.place(relx = 0.85, rely = 0.43)

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
            
        entry = tkinter.Entry(window, width=20)
        entry.insert(0,'File_name')
        
        entry2 = tkinter.Entry(window,width=20)
        entry2.insert(0,'Copied_file_name')
        
        entry.place(relx=0.63,rely=0.50,anchor=tkinter.CENTER)
        entry2.place(relx=0.75, rely=0.50, anchor = tkinter.CENTER)
        
        button_test = tkinter.Button(window, text = "Submit",command=get_input)
        button_test.place(relx=0.82, rely = 0.485)

        cancel_button = tkinter.Button(window,text="Cancel",command=cancel)
        cancel_button.place(relx = 0.88, rely = 0.485)
        

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

        entry = tkinter.Entry(window, width=20)
        entry.insert(0,'Folder name')
        
        entry2 = tkinter.Entry(window,width=20)
        entry2.insert(0,'Copied_folder_name')
        
        entry.place(relx=0.63,rely=0.565,anchor=tkinter.CENTER)
        entry2.place(relx=0.75, rely=0.565, anchor = tkinter.CENTER)
        
        button_test = tkinter.Button(window, text = "Submit",command=get_input)
        button_test.place(relx=0.82, rely = 0.565)

        cancel_button = tkinter.Button(window,text="Cancel",command=cancel)
        cancel_button.place(relx = 0.88, rely = 0.565)

    #initlializing Graphical User Interface
    window = tkinter.Tk()    

    #title of Graphical User Interface
    window.title("VEM - Virtual Environment Management Program")

    #styles the buttons
    style = ttk.Style(window)
    style.theme_use('classic')

    #photo that will be used as icon, must be present in directory
    #icon_photo = tkinter.PhotoImage(file = 'cleanerrr.png') 
      
    # Setting icon of master window, this icon appears on task bar
    #window.iconphoto(False, icon_photo)

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
    #scan_for_files_and_folders()
    #scan_sub_files_and_folders()

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
    menu = tkinter.Menu(window, bg = "white")
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

    #Buttons For GUI
    #Open File Button
    Open_File_Button1 = tkinter.Button(window, bg = "white", text = "OPEN FILE", command = Open_File_Button, font = ("Times New Roman", 18))
    Open_File_Button1.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    #Copy File Button
    Copy_File_Button1 = tkinter.Button(window, bg = "white",text = "COPY FILE", command = Copy_File_Button, font = ("Times New Roman", 18))
    Copy_File_Button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #Copy Folder Button
    Copy_Folder_Button1 = tkinter.Button(window, bg = "white", text = "COPY FOLDER", command = Copy_Folder_Button, font = ("Times New Roman", 18))
    Copy_Folder_Button1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    #Change Directory Button
    Change_dir_button1 = tkinter.Button(window, bg = "white", text = "CHANGE DIRECTORY",command = change_directory_button, font = ("Times New Roman", 18))
    Change_dir_button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    #Delete Single Folder Button
    Delete_single_folder1 = tkinter.Button(window, bg = "white", text = "DELETE SINGLE FOLDER", command = delete_singular_folder, font = ("Times New Roman", 18))
    Delete_single_folder1.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    #Delete Single File Button
    Delete_single_button1 = tkinter.Button(window, bg = "white", text = "DELETE SINGLE FILE", command = delete_singular_file, font = ("Times New Roman", 18))
    Delete_single_button1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    #Delete all files in current working directory
    Delete_all_files_cwd1 = tkinter.Button(window, bg = "white", text = "DELETE ALL FILES (CWD)", command = delete_all_files, font = ("Times New Roman", 18))
    Delete_all_files_cwd1.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    #delete all folders in current working directory
    Delete_all_folders_cwd1 = tkinter.Button(window, bg = "white", text = "DELETE ALL FOLDERS(CWD)", command = delete_all_folders, font = ("Times New Roman", 18))
    Delete_all_folders_cwd1.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                
    #exit program button, just closes the window and exits the program
    Quit_button1 = tkinter.Button(window, bg = "white", text = "EXIT THE PROGRAM", command = destroy_all_windows,font = ("Times New Roman",18))
    Quit_button1.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    print(sys.platform)
    #running the window
    window.mainloop()
    
if __name__ == '__main__':
    generate_gui()
