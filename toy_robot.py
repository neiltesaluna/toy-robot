def initial_robot(x_robot, y_robot, current_facing):

    if (x_robot > max_wtable or x_robot < 0) or (y_robot > max_ltable or y_robot < 0):
        print("\nYour robot is off the table!")
        print("Enter your robots position again")
        return initial_robot(x_robot,y_robot,current_facing)

    if current_facing not in looking:
        print("That can't be right...")
        current_facing = input("NORTH, SOUTH, EAST, WEST = ")
        return initial_robot(x_robot,y_robot,current_facing)

    return command(x_robot, y_robot, current_facing)



def command(x_robot, y_robot, current_facing):

    print("What commands did you want to give the robot?")
    print("""
        MOVE
        ROTATE
        REPORT
        REPOSITION
    """)
    user_cmd = input()

    if user_cmd == 'ROTATE':
        return robot_rotate(current_facing)

    if user_cmd == 'REPORT':
        return robot_position(x_robot, y_robot, current_facing)

    if user_cmd == 'MOVE':
        return moving_robot(x_robot, y_robot, current_facing)

    if user_ == 'REPOSITION':
        return reposition(x_robot, y_robot, current_facing)




def robot_position(x_robot, y_robot, current_facing):
    if x_robot > max_wtable or x_robot < 0:
        if x_robot > max_wtable:
        x_robot -= 1
        if x_robot < 0
        x_robot += 1

        print("\nYour robot is going to fall off the table!")

    if y_robot > max_ltable or y_robot < 0:
        if y_robot > max_wtable:
        y_robot -= 1
        if y_robot < 0
        y_robot += 1

        print("\nYour robot is going to fall off the table!")


    print("Your robot is currently at {}, {} facing {}.".format(x_robot,y_robot,current_facing))
    return command(x_robot, y_robot, current_facing)


def reposition(x_robot, y_robot, current_facing):
    x_robot = int(input("x axis = "))
    y_robot = int(input("y axis = "))
    current_facing = input("NORTH, SOUTH, EAST, WEST = ")

    return initial_robot(x_robot,y_robot, current_facing)



def robot_rotate(current_facing):
    rotate_cmd = input("""
which way did you want to turn?
        RIGHT
        LEFT
""")

    if rotate_cmd == 'RIGHT':
        if current_facing == 'NORTH':
            current_facing = 'EAST'
        elif current_facing == 'EAST':
            current_facing = 'SOUTH'
        elif current_facing == 'SOUTH':
            current_facing = 'WEST'
        elif current_facing == 'WEST':
            current_facing = 'NORTH'

    if rotate_cmd == 'LEFT':
        if current_facing == 'NORTH':
            current_facing = 'WEST'
        elif current_facing == 'EAST':
            current_facing = 'NORTH'
        elif current_facing == 'SOUTH':
            current_facing = 'EAST'
        elif current_facing == 'WEST':
            current_facing = 'SOUTH'

    else:
        print("That's not a vaild input!")

    return robot_position(x_robot, y_robot, current_facing)




def moving_robot(x_robot, y_robot, current_facing):
    user_cmd = input("""
which way did you want to turn?
        FORWARD
        BACK
""")
    if user_cmd == 'FORWARD':
        move_back(x_robot, y_robot, current_facing)
    if user_cmd == 'BACK':
        move_forward(x_robot, y_robot, current_facing)
    else:
        print("That's not a vaild input!")




def move_back(x_robot, y_robot, current_facing):

    if current_facing == 'NORTH':
        x_robot -= 1
    elif current_facing == 'EAST':
        y_robot -= 1
    elif current_facing == 'SOUTH':
        x_robot += 1
    elif current_facing == 'WEST':
        y_robot += 1

    else:
        print("That can't be right...")

    return robot_position(x_robot, y_robot, current_facing)


def move_forward(x_robot, y_robot, current_facing):

    if current_facing == 'NORTH':
        x_robot += 1
    elif current_facing == 'EAST':
        y_robot += 1
    elif current_facing == 'SOUTH':
        x_robot -= 1
    elif current_facing == 'WEST':
        y_robot -= 1

    else:
        print("That can't be right...")

    return robot_position(x_robot, y_robot, current_facing)



looking = ['NORTH','EAST','SOUTH','WEST']

# initial table size and positioning of the robot is defined here

max_wtable = int(input("What is the width of this table? "))
max_ltable = int(input("What is the length of this table? "))

print("For a table of {}W x {}L".format(max_wtable,max_ltable))
print("\nPlease enter where you want to put the robot")

x_robot = int(input("x axis = "))
y_robot = int(input("y axis = "))
current_facing = input("NORTH, SOUTH, EAST, WEST = ")

initial_robot(x_robot,y_robot, current_facing)
