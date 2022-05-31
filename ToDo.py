from operator import index
import os
#Generates the ToDos' database if it's not available
if not os.path.exists("Database.py"):
    File = open("Database.py", "x")
    File.write("ToDos = []")
    File.close()
#Imports the database
from Database import *
#Prints the welcome text
print("\n" + "Welcome to your To Do list".center(os.get_terminal_size()[0]))
#Program's loop
while True:
    command = input("Command: ").lower()
    #Opens this programs repository on github so the user can read the readme for more info
    if command == "help":
        from webbrowser import open as openURL
        openURL("https://github.com/Arman-sm/Learning-python")
        print("The program opened this project's github repository you can read the readme to learn more.")
    #Adds the input(s) to the ToDos list variable
    elif "add" in command:
        if "m=" in command:
            for item in range(int(command[command.index("m=")+2 : ])):
                ToDos.append(input("Add task: "))
        else:
            ToDos.append(input("Add task: "))
    #Gives you a list of all the things in the to do with an index
    elif command == "list":
        for Index, item in enumerate(ToDos):
            print(f"<{Index+1}>: {item}")
    #Deletes the database and regenerate it with the new data
    elif command == "save":
        File = open("Database.py", "w")
        File.write("ToDos = " + str(ToDos))
        File.close()
    #If the user enters a wrong command this is going to appear
    else:
        print("Invalid Command! You can check the documentation with entering the (help) command")