from importlib import reload
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
#region functions
def selectionIndex(Input):
    result = [0, 0]
    #Default selection for multi items
    selection = [0, 0]
    #Deconstructs the input
    Input = Input.split(" ")
    Input.insert(0,"0")
    #Removes empty items
    for idx, item in enumerate(Input):
        if item == "":
            del Input[idx]
    #Multi items
    if "from" in Input:
        selection[0] = Input.index("from")+1 
    elif "to" in Input:
        result[0] = 1
    if "to" in Input:
        selection[1] = Input.index("to")+1
    #Single item
    elif not "from" in Input:
        result[0] = int(Input[-1])
        result[1] = int(Input[-1])
    #For just one of the multi item features
    else:
        result[1] = len(ToDos)
    #Converting index of the indexes into indexes
    result = [result[0] + int(Input[selection[0]]), result[1] + int(Input[selection[1]])]
    #reversing values between the two ends so the start won't be more than the end
    if  result[0] > result[1]:
        result[0], result[1] = result[1], result[0]

    return result

def printList(listOfItems):
    for Index, item in enumerate(listOfItems):
            print(f"<{Index+1}>: {item}")
#endregion

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
        printList(ToDos)
    #Deletes the database and regenerate it with the new data
    elif command == "save":
        File = open("Database.py", "w")
        File.write("ToDos = " + str(ToDos))
        File.close()
    #Discard the changes and restores the not updated version of the list available in the database
    elif command == "restore":
        if input("Are you sure you want to discard the changes you made lastly? (y/n): ") == "y":
            import Database
            reload(Database)
            ToDos = Database.ToDos
    #Removes items you want
    elif "remove" in command:
        selection = selectionIndex(command)
        printList(ToDos[idx] for idx in range(selection[0]-1, selection[1]))
        if input("Are you sure you want to delete all of the list above? (y/n): ") == "y":
            for idx in range(selection[1]-1, selection[0]-2, -1):
                ToDos.pop(idx)
    #Clears the terminal
    elif command == "clear":
        os.system("cls")
    #If the user enters a wrong command this is going to appear
    else:
        print("Invalid Command! You can check the documentation with entering the (help) command")