from turtle import *
from time import *
from random import randint
#Initializing needed variables
size = 2
level = 0
chances = 0
#Turtle setup
setup(size*50+50, size*50+50)
tracer(0)
ht()
pu()
#Database
#0 : empty
#1 : selected but wrong
#2 : correct but not selected
#3 : correct and selected
dataGrid = list()
#Colors
trueColors = {
    0 : "#ffc642",
    1 : "red",
    2 : "lightGreen",
    3 : "green"}
manipulatedColors = {
    0 : "#ffc642",
    1 : "blue",
    2 : "#ffc642",
    3 : "blue"}
#Functions
def refresh(spoil=False, delay=0):
    if spoil:
        smartColor = trueColors
    else:
        smartColor = manipulatedColors
    for y, row in enumerate(dataGrid):
        for x, item in enumerate(row):
            color(smartColor[item])
            #region Drawing a circle
            goto(x*50+25-size*50/2, y*50+25-size*50/2-25)
            pd()
            begin_fill()
            circle(25)
            end_fill()
            pu()
            #endregion
    update()
    sleep(delay)
def isLost(shelf=dataGrid):
    for row in shelf:
        for value in row:
            if value == 1:
                return True
    return False
def placeGreens():
    global level
    global chances
    global dataGrid
    global size
    refresh(True, 1)
    if isLost(dataGrid):
        clear()
        size = 2
        level = 0
        setup(size*50+50, size*50+50)
        print("\nYou lost!\nBack to level zero ⬇")
    elif level > 0.5 * size**2:
        clear()
        size += 1
        setup(size*50+50, size*50+50)
    level += 1
    chances = level
    dataGrid = [[0 for x in range(size)] for y in range(size)]
    for green in range(level):
        while True:
            random = [randint(0, len(dataGrid)-1), randint(0, len(dataGrid)-1)]
            if dataGrid[random[0]][random[1]] != 2:
                dataGrid[random[0]][random[1]] = 2
                break
    refresh(False, 0.1)
    refresh(True, 1)
    refresh(False)
def guessManager(x, y):
    global dataGrid
    global chances
    global level
    try:
        x, y = int(x+len(dataGrid)*50/2)//50, int(y+len(dataGrid)*50/2)//50
        if dataGrid[y][x] == 0 or dataGrid[y][x] == 2:
            dataGrid[y][x] += 1
            chances -= 1
        else:
            dataGrid[y][x] -= 1
            chances += 1
        refresh()
        if chances < 1:
            placeGreens()
    except:
        pass
#Drawing initial circles
placeGreens()
refresh(True, 1)
refresh()
#Mouse event handler
onscreenclick(guessManager)
#Keys event handlers

done()