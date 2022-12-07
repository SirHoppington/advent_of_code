
# Day 6 part 1 function
def day7_pt1():
    file = open('day7/directories.txt', 'r')
    lines = file.readlines()
    stripped = [line.strip().split() for line in lines if "ls" not in line]
    #print(stripped)
    #values = [ line for line in stripped if "cd" not in line]
    values = [line for line in stripped if ".." not in line]
    #print(values)
    #keys = [x[1] for x in values if "ls" in x]
    #values = [x[0] for x in values if "ls" not in x]
    #print(keys)
    #print(values)
    #print(values)
    #print(values)
    new_dict = {}
    #for x in range(1, len(values)):
    #for x in values:
    for x in range(1, len(values)):
        #if "cd" in x[0] or "dir" in x[0]:
        if "cd" in values[x] or "dir" in values[x]:
        #if x[1] == "ls":
            print(values[x][1])
            print(values[x])
            #values.pop(x)
            #new_dict[values[x][0]] = []
            #print(new_dict)
            #print(values.pop(x))
        else:
            continue
            #popped = values.pop(x)
            #print(popped)
            #new_dict[values[x - 1]].insert(0, popped)
    #print(new_dict)
    ## Comprehend over 2 seperate lists:
    #comprehension = { k:v[0] for k, v in zip(keys, values)}
    #print(comprehension)
    #print(file_size)
    #dict = {x[0]:x[1] for x in stripped}
    #dict = {x[1]:x[0] for x in stripped if "cd" not in x}
    #print(dict)