############################
#   Zig-zag turtle walk.   #
#   Date: 17 June, 2023.   #
# .  By Nextcodecamp.       #
############################
print("Turtle by Nextcodecamp")
vegetable = 5
posx = 2
posy = 2
posveg = [[4, 3, "broccoli"], [8, 3, "carrot"], [8, 5, "carrot"],
          [2, 6, "lettuce"], [5, 7, "broccoli"]]
broccoli = 0
carrot = 0
lettuce = 0


def turtleWalk():
    global vegetable
    global posx, posy, broccoli, carrot, lettuce
    direction = "RIGHT"
    while (vegetable != 0 or (posx == 9 and posy == 9)):
        print("current position:", posx, posy)  # current position
        for x in posveg:  # check vegetable
            if (posx == x[0] and posy == x[1]):
                vegetable = vegetable - 1
                if (vegetable == 0):  #we need it to break from loop without  doing any action
                    break
                if (x[2] == "broccoli"):
                    print("grab broccoli at ", posx, posy)
                    broccoli = broccoli + 1
                elif (x[2] == "carrot"):
                    print("grab carrot at ", posx, posy)
                    carrot = carrot + 1
                elif (x[2] == "lettuce"):
                    print("grab lettuce at ", posx, posy)
                    lettuce = lettuce + 1

        if (direction == "RIGHT"):
            posx = posx + 1
            print("RIGHT 1 step to ", posx, posy)
        if (direction == "LEFT"):
            posx = posx - 1
            print("LEFT 1 step to ", posx, posy)
        if (posx == 9 or posx == 1):   #check if reach the last/first cell
            posy = posy + 1
            print("MOVE")    #change row
            if (posx == 9):  #change direction
                direction = "LEFT"
            else:
                direction = "RIGHT"
print("Start position (x,y):", posx,posy)
turtleWalk()
if (vegetable == 0):
    print("I am full.")