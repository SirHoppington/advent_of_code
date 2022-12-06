
# Day 4 part 1 function
def day4_pt1(lines):
    counter = 0
    for line in lines:
        x = line.split(",")
        elf1 = x[0].split("-")
        elf2 = x[1].split("-")


        elf1_range = list(range(int(elf1[0]), int(elf1[1]) + 1))
        elf2_range = list(range(int(elf2[0]), int(elf2[1]) + 1))
        elf1_match = [x for x in elf1_range if x in elf2_range]
        elf2_match = [x for x in elf2_range if x in elf1_range]
        # Check if Elf 1 match is equal to all of Elf 1's section
        if elf1_match == list(elf1_range):
            counter +=1
        # Check if Elf 2 match is equal to all of Elf 2's section
        elif elf2_match == list(elf2_range):
            counter +=1
    print(counter)
    return counter
