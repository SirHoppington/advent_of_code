
# function to open text file, strip new line break and save as a list.
def open_file(file):
    file = open(file, 'r')
    lines = file.readlines()
    new_lines = [line.strip() for line in lines]
    return new_lines