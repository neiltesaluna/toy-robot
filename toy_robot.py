from sys import argv

script, filename = argv
commands_file = open(filename, 'r')


# unpacking the robot commands
def robot_commands(commands_file):

    for line in commands_file:

        line = line.strip('\n')
        print(line,"\n")

        if "PLACE " in line:
            place(line)

        if "REPORT" in line:
            report()

        if "MOVE" in line and on_table:
            move(line)

        if "RIGHT" in line and on_table:
            rotate(line)

        if "LEFT" in line and on_table:
            rotate(line)


    x_pos, y_pos, f_pos = unpack_position()
    print("We've reached the end of our robot commands.")
    print(f"Your robots final position is at:\n\nX:{x_pos}\nY:{y_pos}\nF:{f_pos}\n")
    print("THANKS FOR PLAYING!")




def position_check(x_pos, y_pos, f_pos):

    global on_table

    x_range = x_pos in range(0, max_wtable + 1)
    y_range = y_pos in range(0, max_ltable + 1)
    f_range = f_pos in facing_directions
    range_check = x_range and y_range and f_range

    if range_check:
        on_table = True
        current_position(x_pos, y_pos, f_pos)

    elif not f_range:
        print("What direction is that?!\n")
        on_table = False

    elif not x_range and on_table:
        if x_pos > max_wtable:
            x_pos -= 1
        elif x_pos < 0:
            x_pos += 1
        print("Your robot is going to fall off the table!\n")
        current_position(x_pos, y_pos, f_pos)

    elif not y_range and on_table:
        if y_pos > max_ltable:
            y_pos -= 1
        elif y_pos < 0:
            y_pos += 1
        print("Your robot is going to fall off the table!\n")
        current_position(x_pos, y_pos, f_pos)

    else:
        print("The robots not on the table!\n")



def current_position(x_pos, y_pos, f_pos):

    global saved_position

    pos_current = [x_pos, y_pos, f_pos]
    saved_position.clear()
    saved_position.extend(pos_current)

    print("---",x_pos, y_pos, f_pos,"---\n")



def report():

    global on_table

    if on_table:
        x_pos, y_pos, f_pos = unpack_position()
        print(f"Your robot is currently at:\n\nX:{x_pos}\nY:{y_pos}\nF:{f_pos}\n")


    else:
        print("Your robot is in your hand.\n")



def place(line):

    global on_table

    cmd_strip = line.strip('PLACE ')
    place_cmd = cmd_strip.split(',')

    x_pos = int(place_cmd[0])
    y_pos = int(place_cmd[1])
    f_pos = place_cmd[2]

    position_check(x_pos, y_pos, f_pos)



def unpack_position():

    global saved_position

    x_pos = int(saved_position[0])
    y_pos = int(saved_position[1])
    f_pos = saved_position[2]

    return x_pos, y_pos, f_pos



def move(line):

    x_pos, y_pos, f_pos = unpack_position()

    if f_pos == 'NORTH':
        y_pos += 1
    elif f_pos == 'EAST':
        x_pos += 1
    elif f_pos == 'SOUTH':
        y_pos -= 1
    elif f_pos == 'WEST':
        x_pos -= 1

    position_check(x_pos, y_pos, f_pos)



def rotate(line):


    x_pos, y_pos, f_pos = unpack_position()

    if line == "LEFT":

        if f_pos == 'NORTH':
            f_pos = 'WEST'
        elif f_pos == 'EAST':
            f_pos ='NORTH'
        elif f_pos =='SOUTH':
            f_pos = 'EAST'
        elif f_pos == 'WEST':
            f_pos = 'SOUTH'

    if line == "RIGHT":

        if f_pos == 'NORTH':
            f_pos = 'EAST'
        elif f_pos == 'EAST':
            f_pos ='SOUTH'
        elif f_pos =='SOUTH':
            f_pos = 'WEST'
        elif f_pos == 'WEST':
            f_pos = 'NORTH'

    position_check(x_pos, y_pos, f_pos)




# global variable
saved_position = []
on_table = False


# table dimensions defined here
max_wtable = 5
max_ltable = 5

# robot facing options
facing_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

print("For a table of {}W x {}L".format(max_wtable,max_ltable))

robot_commands(commands_file)
