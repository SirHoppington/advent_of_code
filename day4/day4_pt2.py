file = open('cleaning.txt', 'r')
lines = file.readlines()

counter_pt2 = 0
for line in lines:
    line = line.split()
    x = str(line[0]).split(",")
    elf1 = x[0].split("-")
    elf2 = x[1].split("-")

    elf1_range = list(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2_range = list(range(int(elf2[0]), int(elf2[1]) + 1))
    elf1_match = [x for x in elf1_range if x in elf2_range]
    #counter +=1
    if elf1_match:
        counter_pt2+=1
print(counter_pt2)
