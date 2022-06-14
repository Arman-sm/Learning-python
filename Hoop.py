from time import time

print("Hi, welcome to this game named (Hoop)\nYou have 5 seconds for each turn! - Type * instead of hoop!")

scores = list()

while True:
    lost = False
    cyclesCount = 0
    cycleLength = int(input("How long should each cycle of saying hoop take? "))
    score = 0
    
    while not lost:    
        #Computer's guess
        cyclesCount += 1
        if cyclesCount % cycleLength == 0:
            print("Program: *")
        else:
            print("Program:", cyclesCount, sep=" ")

        #Player's guess
        cyclesCount += 1
        inputTime = time()
        playerInput = input("Player: ")

        if time() - inputTime > 5 or (playerInput != str(cyclesCount) and cyclesCount % cycleLength != 0) or playerInput != "*" and cyclesCount % cycleLength == 0:
            scores.append(score)
            lost = True
        else:
            score += 1

    print("You lost!\n", "Scores:", "-" * 10, sep="\n")
    for idx, score in enumerate(sorted(scores, reverse=True)):
        print(f"<{idx + 1}>: {score}", "⭐" if idx == 0 else "", sep=" ")

    if input("Would you like to play again (y/n)?").lower() != "y":
        exit()