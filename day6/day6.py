
# Day 6 part 1 function
def day6_pt1():
    input = open('day6/datastream.txt', 'r')
    data = input.read()
    input.close()
    count = 0
    for char in range(1, len(data) - 3):
        count += 1
        if data[char] != data[char + 1] and data[char] != data[char + 2] and data[char] != data[char + 3]:
            if data[char + 1] != data[char + 2] and data[char + 1] != data[char + 3]:
                if data[char + 2] != data[char + 3]:
                    count += 4
                    break
    return count
