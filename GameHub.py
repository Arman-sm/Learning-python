#Importing dependencies
from importlib import *
from os import path
from os import system
from os import listdir
from subprocess import run
#Initializing variables
commands = [["detect", {"-p" : ".", "-f" : False, "-s" : False}], ["clear"], ["exit"], ["config", {"-t" : "save", "-p" : "config.py"}]]
#Importing the config if available
if path.isfile("config.py"):
    configFile = import_module("config")
    games = configFile.config["games"]
else:
    configFile = ""

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
                    command.update({tag : (commandChunks[index+2] if commandChunks[index+2][0] != "-" else True) if len(commandChunks) >= index + 3 else True})
            return command
    return "Command not found"

def selectionTool(listOfThings):
    #Deconstructs the input
    Input = ["", ""]
    listOfThings = [[item, True] for item in listOfThings]
    while all([False if Input[1] == endValue else True for endValue in ["exit", "quit", "done"]]):
        Input = input("> ").split(" ")
        Input.insert(0,"0")

        #Removes empty items in the list
        for idx, item in enumerate(Input):
            if item == "":
                del Input[idx]

        result = [0, 0]
        markAs = False if Input[1] == "not" else True
        selection = [0, 0]
                    
        if "contain" in Input:
            for idx, item in enumerate(listOfThings):
                if Input[-1] in item[0]:
                    listOfThings[idx][1] = markAs

        elif "list" in Input:
            for idx, item in enumerate(listOfThings):
                print(f"<{idx+1}> {item[0]}", "✅" if item[1] else "❌")
        elif Input[1] == "all":
            for idx in range(len(listOfThings)):
                listOfThings[idx][1] = markAs
        elif "from" in Input or "to" in Input or Input[-1].isdigit():
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
                result[1] = len(listOfThings)
            #Converting index of the indexes into indexes
            result = [result[0] + int(Input[selection[0]]) - 1, result[1] + int(Input[selection[1]])]
            #reversing values between the two ends so the start won't be more than the end
            if  result[0] > result[1]:
                result[0], result[1] = result[1], result[0]
            
            result = [len(listOfThings) if result[idx] > len(listOfThings) else 0 if result[idx] < 0 else result[idx] for idx in range(2)]
            

            for idx in range(result[0], result[1]):
                listOfThings[idx][1] = markAs

    Result = []
    for item in listOfThings:
        if item[1]:
            Result.append(item[0])
    return Result

#Commands
def clear(_):
    system("cls")

def quit(_):
    exit()

def config(command):
    command["-t"] = command["-t"].lower()
    global configFile
    global games
    if command["-t"] == "save":
        configFile = open(command["-p"], "w")
        configFile.write("config = {'games' : "+ str(games)+"}")
        configFile.close()
    elif command["-t"] == "read" and path.isfile(command["-p"]):
        if "configFile" in globals():
            reload(configFile)
        else:
            import_module(command["-p"])
        configFile = import_module("config")
        games = configFile.config["games"]
#Detects games
def detect(command):
    if command["-f"]:
        if path.splitext(command["-p"])[1] == ".py" and path.isfile(command["-p"]):
            validFiles = [command["-p"]]
        else:
            print("File not found")
            return "!"
    else:
        if command["-p"] != "." and not path.isdir(command["-p"]):
            print("Directory not found")
            return "!"
        validFiles = []
        for file in listdir(command["-p"]):
            if path.splitext(file)[1] == ".py":
                validFiles.append(file)
    
    if command["-s"]:
        validFiles = selectionTool(validFiles)
    global games
    if input("Are you sure? This action might cause malicious activities to happen on your computer! (y/n): ").lower() == "y":
        for game in validFiles:
            if game != path.basename(__file__):
                games.update({path.splitext(game)[0] : path.join(command["-p"] if command["-p"] != '.' else '', game)})
                
#Main loop
while(True):
    command = bakeCommand(input("Command: "))
    if type(command) == dict:
        if command["command"] in [command[0] for command in commands]:
            globals()[command["command"]](command)
        else:
            run(games[command["command"]], shell=True)
    else:
        print(command)