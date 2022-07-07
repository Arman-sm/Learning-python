import importlib
from operator import index
import os
from posixpath import split
#Generates the ToDos' database if it's not available
if not os.path.exists("Database.py"):
    File = open("database.py", "x")
    File.write("ToDos = []")
    File.close()
#Imports the database
databaseName = "database"
database = importlib.import_module(databaseName)
ToDos = database.ToDos
#Prints the welcome text
print("\n" + "Welcome to your To-Do list".center(os.get_terminal_size()[0]))
#region functions
def selectionIndex(Input):
    result = [0, 0]
    #Default selection for multi items
    selection = [0, 0]
    if "all" in Input:
        return [1, len(ToDos)]
    else:
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
    for idx, item in enumerate(listOfItems):
        print(f"<{idx+1}>: {item[0]} (", ("❌" if item[1] == 0 else "✅"), ")", sep="")
        
#endregion

#Program's loop
while True:
    command = input("Command: ").lower()
    try:
        #Opens this programs repository on github so the user can read the readme for more info
        if command == "help":
            from webbrowser import open as openURL
            openURL("https://github.com/Arman-sm/Learning-python")
            print("The program opened this project's github repository you can read the readme to learn more.")
        #Adds the input(s) to the ToDos list variable
        elif command.split(" ")[0] == "add":
            if "m=" in command:
                for item in range(int(command[command.index("m=")+2 : ])):
                    ToDos.append([input("Add task: "), 0])
            else:
                ToDos.append([input("Add task: "), 0])
        #Gives you a list of all the things in the to do with an index
        elif command == "list":
            printList(ToDos)
        #Changes an item's status
        elif "status" in command:
            selection = selectionIndex(command)
            for idx in range(selection[0]-1, selection[1]):
                ToDos[idx][1] = 1 if "check" in command or "done" in command else 0
        #Removes items you want
        elif "remove" in command:
            selection = selectionIndex(command)
            printList(ToDos[idx] for idx in range(selection[0]-1, selection[1]))
            if input("Are you sure you want to delete all of the list above? (y/n): ") == "y":
                for idx in range(selection[1]-1, selection[0]-2, -1):
                    ToDos.pop(idx)
        #Deletes the database and regenerate it with the new data
        elif command == "save":
            File = open(databaseName+".py", "w")
            File.write("ToDos = " + str(ToDos))
            File.close()
        #Clears the terminal
        elif command == "clear":
            os.system("cls")
            print("\n" + "Your To-Do list".center(os.get_terminal_size()[0]))
        #Things related to database like saving, restoring and database management
        elif "database" in command or "db" in command:
            #Manages databases
            command = [item for item in command.split(" ")]
            for idx, item in enumerate(command):
                if item == "":
                    del command[idx]
             #Discard the changes and restores the not updated version of the list available in the database
            if command[1] == "restore":
                if input("Are you sure you want to discard the changes you made lastly? (y/n): ") == "y":
                    importlib.reload(database)
                    ToDos = database.ToDos
            elif command[1] == "switch":
                databaseName = command[command.index("switch")+1]
                database = importlib.import_module(databaseName)
                ToDos = database.ToDos
            elif command[1] == "new":
                File = open(command[command.index("new")+1]+".py", "x")
                File.write("ToDos = []")
                File.close()
                databaseName = command[command.index("new")+1]
                database = importlib.import_module(databaseName)
                ToDos = database.ToDos
            elif command[1] == "saveas":
                File = open(command[command.index("saveas")+1]+".py", "x")
                File.write("ToDos = " + str(ToDos))
                File.close()
            elif command[1] == "add":
                print()

        #Exits the program
        elif command == "exit":
            if input("Are you sure you want to exit? (make sure to save your to-do) (y/n): ") == "y":
                exit()
        #If the user enters a wrong command this is going to appear
        else:
            print("Invalid Command! You can check the documentation with entering the (help) command")
    except:
        print("Something went wrong!")