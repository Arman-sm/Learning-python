from time import time

print("Hi, welcome to this game named (Hoop)\nYou have 5 seconds for each turn! - Type * instead of hoop!")

lost = False
cyclesCount = 0
cycleLength = int(input("How long should each cycle of saying hoop take? "))

while not lost:    
    #Computer's guess
    cyclesCount += 1
    if cyclesCount % cycleLength == 0:
        print("Program: *")
    else:
        print("Program:", cyclesCount)
    
    #Player's guess
    cyclesCount += 1
    inputTime = time()
    playerInput = input("Player: ")

    if time() - inputTime > 5:
        lost = True
    elif playerInput != "*" and cyclesCount % cycleLength == 0:
        lost = True
    elif playerInput != str(cyclesCount) and cyclesCount % cycleLength != 0:
        lost = True

print("Gameover!")