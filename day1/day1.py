file = open('elves.txt', 'r')
lines = file.readlines()

total = []
calories = 0
top_three = []
for line in lines:
    if line != "\n":
        line.strip()
        x = int(line)
        calories += x
    elif line == "\n":
        total.append(calories)
        calories = 0
# find top three calories in list
top_three.append(max(total))
total.remove(max(total))
top_three.append(max(total))
total.remove(max(total))
top_three.append(max(total))

print(sum(top_three))