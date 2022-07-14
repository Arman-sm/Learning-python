from importlib import *
from os import *

games = {}

def deconstruct(value):
    chunks = []
    for chunk in value.split():
        if chunk != "":
            chunks.append(chunk)
    return chunks

def autoDetectGames(filePath = "."):
    if filePath != "." and not path.isdir(filePath):
        print("Directory not found.")
        
    validFilesList = []
    for file in listdir(filePath):
        if path.splitext(file)[1] == ".py":
            validFilesList.append(path.splitext(file)[0])
    global games
    if input("Are you sure? They might cause malicious activities on your computer. (y/n): ").lower() == "y":
        for game in validFilesList:
            games.update({game : path.join(filePath if filePath != '.' else '', game)})
            print(games.items())

while(True):
    command = input("Command: ")
    if "autoDetect" in command:
        if "-p" in command:
            command = deconstruct(command)
            autoDetectGames(command[command.index("-p")+1])
        else:
            autoDetectGames()
    elif command in games:
        game = __import__(games[command])
        game.main()
    elif command == "exit" :
        exit()
    elif command in ["clear", "cls"]:
        system("cls")