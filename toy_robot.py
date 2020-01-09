from sys import exit, argv

script, filename = argv
commands_file = open(filename, 'r')

# unpacking the robot commands into a list
def robot_commands(commands_file):
    line = commands_file.read()
    cmd_split = line.split()
    return cmd_split




# table dimensions defined here
max_wtable = 5
max_ltable = 5

print("For a table of {}W x {}L".format(max_wtable,max_ltable))

robot_instructions = robot_commands(commands_file)

print(robot_instructions)
