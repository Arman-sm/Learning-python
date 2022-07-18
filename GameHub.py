from importlib import *
from os import *

games = {}
commands = ["detectDir", "clear", "quit"]


#Organizing the command in a dict
def bakeCommand(command):
    #Separating commands and tags for organizing them
    commandChunks = []
    for chunk in command.split():
        if chunk != "":
            commandChunks.append(chunk)
    #Checking if the command is available in the games or in the main commands list
    if commandChunks[0] in commands or commandChunks[0] in games:    
        #Adding the main command name to the command info
        command = {"command" : commandChunks[0]}
        #Adding the tags to the command info
        for index, tag in enumerate(commandChunks[1:]):
            if tag[0] == "-":
                command.update({tag : (commandChunks[index+2] if commandChunks[index+2][0] != "-" else True) if len(commandChunks) >= index + 2 else True})
        if command["command"] in commands or command["command"] in games:
            return command
    else:
        return "Command not found"
#Commands
def clear(_):
    system("cls")

def quit(_):
    exit()

def detectDir(command):
    if not "-p" in command:
        command.update({"-p" : "."})
    elif command["-p"] != "." and not path.isdir(command["-p"]):
        print("Directory not found")
        
    validFiles = []
    for file in listdir(command["-p"]):
        if path.splitext(file)[1] == ".py":
            validFiles.append(path.splitext(file)[0])
    global games
    if input("Are you sure? They might cause malicious activities on your computer! (y/n): ").lower() == "y":
        for game in validFiles:
            if game != path.splitext(path.basename(__file__))[0]:
                games.update({game : path.join(command["-p"] if command["-p"] != '.' else '', game)})
                print(games.items())

#Main loop
while(True):
    command = bakeCommand(input("Command: "))
    if type(command) == dict:
        if command["command"] in globals():
            globals()[command["command"]](command)
        elif games[command["command"]] in games:
            game = __import__(games[command["command"]])
            game.main()
    else:
        print(command)