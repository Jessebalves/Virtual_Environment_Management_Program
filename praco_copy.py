import tkinter
import sys
import os
import shutil
import time

window = tkinter.Tk()
window.title("VEM - Virtual Environment Management Program")
window.geometry("1920x1080")
text_widget = tkinter.Text(window,height =1920, width =1080,font = ("Times New Roman", 20))
text_widget.pack()

#function to exit program
def exit_program():
    #for value in thanks:
     #   print(value,end="")
      #  time.sleep(0.003)
    window.destroy()
    for value in thanks:
        print(value,end="")
        time.sleep(0.003)
    sys.exit(0)

#call this to instantly generate another GUI, still working on closing the original. 
def generate_gui():
    window = tkinter.Tk()
    window.title("VEM - Virtual Environment Management Program")
    window.geometry("1920x1080")
    text_widget = tkinter.Text(window,height =1920, width =1080,font = ("Times New Roman", 20))
    text_widget.pack()
    OP_Message = ('Operating System on machine: ' + os.name)
    text_widget.insert(tkinter.END,OP_Message)
    Change_dir_button = tkinter.Button(window, text = "CHANGE DIRECTORY",command= clicked_button, font = ("Times New Roman", 15))
    Change_dir_button.place(x=1200, y= 300)
    Quit_button = tkinter.Button(window,text = "QUIT PROGRAM", command = exit_program)
    Quit_button.place(x=1200,y=400)
    text_widget.insert(tkinter.END,"\n")
    text_widget.insert(tkinter.END,"Current Working Directory: ")
    text_widget.insert(tkinter.END,os.getcwd())
    text_widget.insert(tkinter.END,"\n")
    text_widget.insert(tkinter.END,'\nFolders found in Local Directories: ')
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
    

#function that is associated with the tkinter buttons created
def clicked_button():
    print("Change directory test button")
    #generate_gui()
    user_message3 = input("Which directory homie")
    os.chdir(user_message3)
    generate_gui()
    

#this function has been moved
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
            

#This is an example of tkinter module
#create Graphical User interface
#root = tkinter.Tk()

#title for graphical user interfave
#root.title("VEM - Virtual Environment Management Program")

#size of GUI
#root.geometry("1920x1080")

#text_widget = tkinter.Text(root,height =1920, width =1080,font = ("Times New Roman",30))
#text_widget.pack()


files_local_directory = []
files_sub_directory = []
folders_local_directory = []
folders_sub_directory = []
thanks = "Thank you for checking out my program!"
        
OP_Message = ('Operating System on machine: ' + os.name)
Current_dir = ('\nCurrent working directory: ' + os.getcwd()+ '\n')
print(OP_Message)

scan_for_files_and_folders()
#sub directory for loops
for value in folders_local_directory:
    previous_dir = os.getcwd()
    os.chdir(value)
    for items in os.listdir():
        if os.path.isfile(items):
            files_sub_directory.append(items)
        if os.path.isdir(items):
            folders_sub_directory.append(items)
    os.chdir(previous_dir)

#text_widget.insert(tkinter.END,OP_Message)
#Change_dir_button = tkinter.Button(root, text = "CHANGE DIRECTORY",command= clicked_button, font = ("Comic Sans", 10))
#Change_dir_button.place(x=1200, y= 300)
#Quit_button = tkinter.Button(root,text = "QUIT PROGRAM", command = exit_program)
#Quit_button.place(x=1200,y=400)
#text_widget.insert(tkinter.END,Current_dir)
#text_widget.insert(tkinter.END,"\n")
#text_widget.insert(tkinter.END,'Folders found in Local Directories: ')
#text_widget.insert(tkinter.END,folders_local_directory)
#text_widget.insert(tkinter.END,'\nFolders found in Sub Directories: ')
#text_widget.insert(tkinter.END,folders_sub_directory)
#text_widget.insert(tkinter.END,"\n")
#text_widget.insert(tkinter.END,"\nFiles found in Main Directory: ")
#text_widget.insert(tkinter.END,files_local_directory)
#text_widget.insert(tkinter.END,"\nFiles found in Sub Directory: ")
#text_widget.insert(tkinter.END,files_sub_directory)
#text_widget.insert(tkinter.END,"\n")
#root.mainloop()

print("Operating System on machine: ", os.name)
print("Operating System on machine: ", os.uname_result)
print("Operating System on machine: ", sys.platform)
print("Current working directory: ",os.getcwd(),"\n")

#traverse()

#Print statements
print("Folders found in Local Directories: ",folders_local_directory)
print("Folders found in Sub Directories: ", folders_sub_directory)
print("\n")
print("Files found in Main Directory: ",files_local_directory)
print("Files found in Sub Directory: ",files_sub_directory)
print("\n")

text_widget.insert(tkinter.END,OP_Message)
Change_dir_button = tkinter.Button(window, text = "CHANGE DIRECTORY",command= clicked_button, font = ("Times New Roman", 15))
Change_dir_button.place(x=1200, y= 300)
Quit_button = tkinter.Button(window,text = "QUIT PROGRAM", command = exit_program,font = ("Times New Roman",20))
Quit_button.place(x=1200,y=400)
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

#if __name__ == "__main__":
     
#user_message1 = input("Change Directory? (Enter yes or no)")
#if user_message1 == "yes":
#    user_message1 = input("What would you like to change the directory to?")
#    os.chdir(user_message1)
#    print(os.getcwd())
#elif user_message1 == "no":
#    pass
#user_message2 = input("Would you like to exit the program?")
#if user_message2 == "yes":
#        exit_program()
#elif user_message2 == "no":
#    print("continue from here")
#else:
#    print("sorry we dont quite understand")
#    sys.exit(1)
