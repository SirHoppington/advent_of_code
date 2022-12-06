#from day1.utilities import open_file
#lines = open_file('starting_stack.txt')


def day5_pt1(lines):
    for line in lines[10:]:
        number_of_crates = line[1]
        starting_position = line[3]
        finishing_position = line[5]
        print(f"NUMBER OF CRATES: {number_of_crates}, from: {starting_position} to {finishing_position}")