from collections import defaultdict

# Day 6 part 1 function
def day7_pt1():
    file = open('day7/directories.txt', 'r')
    lines = file.readlines()
    tree = []
    sizes = defaultdict(int)
    for line in lines:
        if  "$ cd" in line:
            s = line.split()[-1]
            if s == '..':
                tree.pop()
            else:
                tree.append(s)
        elif "$ ls" in line:
            continue
        else:
            size = line.split()[-2]
            if size.isdigit():
                size = int(size)
                for i in range(len(tree)):
                    sizes['/'.join(tree[:i+1])] += size
    result = 0
    for key, value in sizes.items():
        if value <= 100_000:
            result += value

    # part 2:
    disk_space = 70000000 - sizes['/']
    required = 30000000 - disk_space
    for size in sorted(sizes.values()):
        if size >= required:
            print(size)
            break

