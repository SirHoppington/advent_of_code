
# Day 6 part 1 function
def day6_pt2():
    file = open('day6/datastream.txt', 'r')
    data = file.read()
    file.close()
    count = 0
    print(len(data))
    for char in range(0, len(data) - 15):
        start = 0
        count += 1
        char_count = 0
        while start <= 13:
            for x in range(start, 13):
                if data[char + start] != data[char + (x + 1)]:
                    char_count += 1
                    if char_count == 91:
                        count += 13
                        print(count)
                        return count
            start += 1
