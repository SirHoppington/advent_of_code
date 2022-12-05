file = open('strategy_guide.txt', 'r')
lines = file.readlines()

# Method 1 iterate through possible fixtures and compare with scores (dictionary):
score = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3,
}
result = []
for line in lines:
    line = line.strip()
    if line in score.keys():
        result.append(score[line])
print(sum(result))


## Method 2: Neverending if statements:
score = 0
for line in lines:
    line = line.strip()
    if line == "A Y":
        score += 8
    elif line == "A X":
        score += 4
    elif line == "A Z":
        score += 3
    elif line == "B X":
        score += 1
    elif line == "B Y":
        score += 5
    elif line == "B Z":
        score += 9
    elif line == "C X":
        score += 7
    elif line == "C Y":
        score += 2
    elif line == "C Z":
        score += 6
print(score)


# Method 3 Python map function:
score = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3,
}

def replace(i):
    i = i.strip()
    if i in score.keys():
        return score[line]

print(sum(list(result)))