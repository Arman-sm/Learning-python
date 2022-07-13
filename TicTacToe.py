from turtle import *
#region Turtle
#region turtle properties
setup(3 * 180 + 10, 3 * 180 + 10) #Rows/Columns * their heights/widths
speed(100)
pensize(5)
#endregion
#region Graphical functions
def go(x, y):
    penup()
    goto(x, y)
    pendown()
#endregion
#region empty pattern
go(-1 * (90+180), -90)
fd(3 * 180)
go(-1 * (90+180), 90)
fd(3 * 180)

right(90)

go(-90, 90 + 180)
fd(3 * 180)
go(90, 90 + 180)
fd(3 * 180)
#endregion
#endregion

#region Functions
def check():
    for side in range(3):
        if data[side][0] + data[side][1] + data[side][2] == valueToPut * 3:
            return [[side, 0], [side, 2]]
        if data[0][side] + data[1][side] + data[2][side] == valueToPut * 3:
            return [[side, 0], [2, side]]
        if data[0][side] + data[1][1] + data[2][2-side] == valueToPut * 3:
            return [[0 , side], [2, 2-side]]
    return False
#endregion
#region Initializing variables
valueToPut = 2 #It keeps if x/o should be put in the database x = 2 and o = 5
data = [ #This data specifies if a block contains x, o or nothing in it
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
translate = { #A translator for translating what's in the data base to "x" or "o"
    2 : "x",
    5 : "O"
}
#endregion

while(True):
    valueToPut = (valueToPut+3)%6
    while(True):
        coords = input(f"Coordinates for {translate[valueToPut]}: ").split()
        if coords[0].isdigit() and coords[-1].isdigit() and len(coords) > 1:
            coords = [int(coords[0]) % 4 - 1, int(coords[-1]) % 4 - 1]
            if data[coords[0]][coords[-1]] == 0:
                data[coords[0]][coords[-1]] = valueToPut
                break
            print("This block is already occupied! Try again.")
            continue
        print("Wrong input!")
    print(data)

    Result = check()
    if Result != False:
        print(f"{translate[valueToPut].upper()} won!")