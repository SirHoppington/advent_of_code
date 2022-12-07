# Calculate unique string character length check
def unique_string(number):
    required_char = 0
    for x in range(1, number + 1):
        required_char += number - 1
        number -= 1
    return required_char


# Day 6 part 1 function
def day6_pt2():
    file = open('day6/datastream.txt', 'r')
    data = file.read()
    file.close()
    count = 0
    required_length = unique_string(14)
    for char in range(0, len(data) - 15):
        start = 0
        count += 1
        char_count = 0
        while start <= 13:
            for x in range(start, 13):
                if data[char + start] != data[char + (x + 1)]:
                    char_count += 1
                    if char_count == required_length:
                        count += 13
                        return count
            start += 1
