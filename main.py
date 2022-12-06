#from day2.day2 import day2_pt1
from day3.day3 import day3_pt1_pt2
from day4.day4 import day4_pt1
from day4.day4_pt2 import day4_pt2
from day5.day5 import day5_pt1
from day5.day5_pt2 import day5_pt2
from utilities import open_file

#Execute day 1 function
#day1_lines = open_file('day1/elves.txt')
#day1_pt1(day1_lines)
#Execute day 2 function
#day2_lines = open_file('day2/strategy_guide.txt')
#day2_pt1(day2_lines)


#Execute day 3 function
day3_lines = open_file('day3/rucksack.txt')
day3_pt1_pt2(day3_lines)


#Execute day 4 function
day4_lines = open_file('day4/cleaning.txt')
day4_pt1(day4_lines)

day4_lines = open_file('day4/cleaning.txt')
day4_pt2(day4_lines)

#Execute day 5 function
day5_pt1()
day5_pt2()
