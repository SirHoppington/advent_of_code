from collections import defaultdict

# Day 6 part 1 function
def day7_pt1():
    file = open('day7/directories.txt', 'r')
    lines = file.readlines()
    tree = []
    sizes = defaultdict(int)
    print(sizes)
    for line in lines:
        if line.startswith('$ cd'):
            s = line.split()[-1]
            if s == '..':
                tree.pop()
            else:
                tree.append(s)
        elif line.startswith('$ ls'):
            continue
        else:
            size = line.split()[-2]
            if size.isdigit():
                size = int(size)
                for i in range(len(tree)):
                    print(tree[:i+1])
                    sizes['/'.join(tree[:i+1])] += size
    result = 0
    for key, value in sizes.items():
        if value <= 100_000:
            result += value
    print(result)