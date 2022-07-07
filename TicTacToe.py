from turtle import *
#region scheme
setup(3 * 180 + 10, 3 * 180 + 10) #Rows/Columns * their heights/widths
speed(100)
pensize(5)
#endregion

pu()
goto(-1 * (90+180), -90)
pd()
fd(3 * 180)
pu()
goto(-1 * (90+180), 90)
pd()
fd(3 * 180)
right(90)
pu()
goto(-90, 90 + 180)
pd()
fd(3 * 180)
pu()
goto(90, 90 + 180)
pd()
fd(3 * 180)
#endregion

valueToPut = 0 #it says x/o should be put in the database
data = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


while(True):
    valueToPut = (valueToPut+0)%3
    while(True):
        coords = input("Coordinates of : ").split()
        coords = [int(coords[0]), int(coords[-1])]
        if data[coords[0]][coords[1]] != 0:
            data[coords[0]][coords[1]] = valueToPut
            break
        print("This block is already occupied! Try again.")
    pu()
    goto()