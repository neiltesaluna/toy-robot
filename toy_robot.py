from sys import exit, argv

script, filename = argv
commands_file = open(filename, 'r')

# unpacking the robot commands into a list
def robot_commands(commands_file):

    for line in commands_file:
        if "PLACE " in line:
            place(line)

def place(line):
    cmd_strip = line.strip('PLACE ')
    place_cmd = cmd_strip.split(',')

    x_pos = int(place_cmd[0])
    y_pos = int(place_cmd[1])
    f_pos = place_cmd[2]

    position_check(x_pos, y_pos, f_pos)

def position_check(x_pos, y_pos, f_pos):

    print(x_pos,y_pos,f_pos)






# table dimensions defined here
max_wtable = 5
max_ltable = 5

print("For a table of {}W x {}L".format(max_wtable,max_ltable))

robot_instructions = robot_commands(commands_file)

print(robot_instructions)
