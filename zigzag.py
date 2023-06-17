############################
#   Zig-zag turtle walk.   #
#   Date: 17 June, 2023.   #
# .  By Nextcodecamp.       #
############################
print("Turtle by Nextcodecamp")
vegetable = 4
posx = 2
posy = 2
posveg = [[4, 3, "broccoli"], [8, 3, "carrot"], [8, 5, "carrot"], [2, 6, "lettuce"], [5, 7, "broccoli"]]

broccoli = 0
carrot = 0
lettuce = 0


def posTurtle():
    turtlepos = {"posx": posx, "posy": posy}
    return turtlepos

def turtleWalk():
    global vegetable
    global posx, posy, broccoli, carrot, lettuce
    while (vegetable != 0 or (posx == 9 and posy == 9)):
        print("move to loc:", posx, posy)  # current position
        if (posx != 9):
            posx = posx + 1
        if (posx == 9):  # reach last cell in row, go to the next row
            posx = 1
            posy = posy + 1
        for x in posveg:  # check vegetable
            if (posx == x[0] and posy == x[1]):
                vegetable = vegetable - 1
                if (x[2] == "broccoli"):
                    print("grab broccoli at ", posx, posy)
                    broccoli = broccoli + 1
                elif (x[2] == "carrot"):
                    print("grab carrot at ", posx, posy)
                    carrot = carrot + 1
                elif (x[2] == "lettuce"):
                    print("grab lettuce at ", posx, posy)
                    lettuce = lettuce + 1


print("Current position:", posTurtle())
turtleWalk()
if (vegetable == 0):
    print("I am full.")
