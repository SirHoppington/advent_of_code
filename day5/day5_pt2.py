
def day5_pt2():
    file = open('day5/starting_stack.txt', 'r')
    lines = file.readlines()
    stacks = {x: [] for x in lines[8].strip().split()}
    for line in lines[:8]:
        stacks["1"] += line[1].strip()
        stacks["2"] += line[5].strip()
        stacks["3"] += line[9].strip()
        stacks["4"] += line[13].strip()
        stacks["5"] += line[17].strip()
        stacks["6"] += line[21].strip()
        stacks["7"] += line[25].strip()
        stacks["8"] += line[29].strip()
        if len(line) > 32:
            stacks["9"] += line[33]
    for line in lines[10:]:
        line = line.split()
        number_of_crates = line[1]
        starting_position = line[3]
        finishing_position = line[5]
        counter = int(number_of_crates)
        crates = []
        while counter > 0:
            counter -= 1
            x = stacks[starting_position].pop(0)
            crates.append(x)
        for crate in reversed(crates):
            stacks[finishing_position].insert(0, crate)
    result = []
    for x, y in stacks.items():
        result.append(y[0])
    return stacks
