from importlib import *
from os import *
import subprocess

games = {}
commands = [["detectDir", {"-p" : "."}], ["clear"], ["quit"]]


#Organizing the command in a dict
def bakeCommand(command):
    if command != "" or command.isspace():
        #Separating commands and tags for organizing them
        commandChunks = []
        for chunk in command.split():
            if chunk != "":
                commandChunks.append(chunk)
        #Checking if the command is available in the games or in the main commands list
        if commandChunks[0] in [command[0] for command in commands] or commandChunks[0] in games:    
            #Adding the main command name to the command info
            command = {"command" : commandChunks[0]}
            #Adding the default tag values if available
            for commandConfig in commands:
                if commandConfig[0] == commandChunks[0] and len(commandConfig) > 1:
                    command.update(commandConfig[1])
            #Adding the tags to the command info
            for index, tag in enumerate(commandChunks[1:]):
                if tag[0] == "-":
                    command.update({tag : (commandChunks[index+2] if commandChunks[index+2][0] != "-" else True) if len(commandChunks) >= index + 2 else True})
            return command
    return "Command not found"
#Commands
def clear(_):
    system("cls")

def quit(_):
    exit()

def detectDir(command):
    if command["-p"] != "." and not path.isdir(command["-p"]):
        print("Directory not found")
        
    validFiles = []
    for file in listdir(command["-p"]):
        if path.splitext(file)[1] == ".py":
            validFiles.append(file)
    print(validFiles)
    global games
    if input("Are you sure? They might cause malicious activities on your computer! (y/n): ").lower() == "y":
        for game in validFiles:
            if game != path.splitext(path.basename(__file__))[0]:
                games.update({path.splitext(game)[0] : path.join(command["-p"] if command["-p"] != '.' else '', game)})

#Main loop
while(True):
    command = bakeCommand(input("Command: "))
    if type(command) == dict:
        if command["command"] in [command[0] for command in commands]:
                globals()[command["command"]](command)
        else:
            subprocess.call(games[command["command"]], shell=True)
    else:
        print(command) 