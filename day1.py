file = open('elves.txt', 'r')
lines = file.readlines()

total = []
calories = 0
for line in lines:
    if line != "\n":
        line.strip()
        x = int(line)
        calories += x
    elif line == "\n":
        total.append(calories)
        calories = 0

print(max(total))