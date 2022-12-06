file = open('strategy_guide.txt', 'r')
lines = file.readlines()

hand = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

result = []
for line in lines:
    line = line.strip()
    if "X" in line:
        if "A" in line:
            result.append(hand["scissors"])
        elif "B" in line:
            result.append(hand["rock"])
        elif "C" in line:
            result.append(hand["paper"])
    elif "Y" in line:
        if "A" in line:
            result.append(hand["rock"] + 3)
        elif "B" in line:
            result.append(hand["paper"] + 3)
        elif "C" in line:
            result.append(hand["scissors"] + 3)
    elif "Z" in line:
        if "A" in line:
            result.append(hand["paper"] + 6)
        elif "B" in line:
            result.append(hand["scissors"] + 6)
        elif "C" in line:
            result.append(hand["rock"] + 6)
print(sum(result))
