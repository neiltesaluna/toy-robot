from sys import exit, argv

script, filename = argv
commands_file = open(filename, 'r')

# unpacking the robot commands into a list
def robot_commands(commands_file, saved_position):

    for line in commands_file:
        if len(saved_position) == 0:
            if "PLACE " in line:
                place(line)
            else:
                robot_commands(commands_file, saved_position)

        if "MOVE" in line:
            move(line, saved_position)


def position_check(x_pos, y_pos, f_pos):

    x_range = x_pos in range(0, max_wtable + 1)
    y_range = y_pos in range(0, max_ltable + 1)
    f_range = f_pos in facing_directions
    range_check = x_range and y_range and f_range


    if range_check:
        current_position(x_pos, y_pos, f_pos)

    elif not x_range:
        if x_pos > max_wtable:
            x_pos -= 1
        elif x_pos < 0:
            x_pos += 1

    elif not y_range:
        if y_pos > max_ltable:
            x_pos -= 1
        elif y_pos < 0:
            x_pos += 1

    else:
        print("That didn't seem like a valid command. We'll skip that one...")
        robot_commands(commands_file, saved_position)


def current_position(x_pos, y_pos, f_pos):

    saved_position = [x_pos, y_pos, f_pos]
    print(f"Your robot is currently at:\nX={x_pos}\nY={y_pos}\nF={f_pos}")

    robot_commands(commands_file, saved_position)



def unpack_position(saved_position):

    x_pos = int(saved_position[0])
    y_pos = int(saved_position[1])
    f_pos = saved_position[2]

    return x_pos, y_pos, f_pos



def place(line):

    cmd_strip = line.strip('PLACE ')
    cmd_strip = cmd_strip.strip('\n')
    place_cmd = cmd_strip.split(',')

    x_pos = int(place_cmd[0])
    y_pos = int(place_cmd[1])
    f_pos = place_cmd[2]
    position_check(x_pos, y_pos, f_pos)



def move(line, saved_position):

    x_pos, y_pos, f_pos = unpack_position(saved_position)

    if f_pos == 'NORTH':
        y_pos += 1
    elif f_pos == 'EAST':
        x_pos += 1
    elif f_pos == 'SOUTH':
        y_pos -= 1
    elif f_pos == 'WEST':
        x_pos -= 1

    position_check(x_pos, y_pos, f_pos)



def rotate(line, saved_position):

    x_pos, y_pos, f_pos = unpack_position(saved_position)

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









# table dimensions defined here
max_wtable = 5
max_ltable = 5
saved_position = []

# robot facing options
facing_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

print("For a table of {}W x {}L".format(max_wtable,max_ltable))

robot_commands(commands_file, saved_position)
