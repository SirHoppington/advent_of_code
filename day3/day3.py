file = open('rucksack.txt', 'r')
lines = file.readlines()

# Create item mapping
items = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "x": 50,
        "Y": 51,
        "Z": 52,
    }


total = 0

for line in lines:
    line = line.strip()
    first_half = [items[x] for x in line[:(int(len(line) / 2))]]
    second_half = [items[x] for x in line[(int(len(line) / 2)):]]
    result = [x for x in first_half if x in second_half]
    total += result[0]

# Part 2:
badge_total = 0
stripped = []
for line in lines:
        line = line.strip()
        result = [items[x] for x in line]
        stripped.append(result)
groups = [stripped[x:x+3] for x in range(0, len(lines), 3)]
for group in groups:
        badge = [x for x in group[0] if x in group[1] and x in group[2]]
        badge_total += badge[0]

print(total)
print(badge_total)
