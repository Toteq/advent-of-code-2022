list_of_items_on_rucksack = open("input_day3.txt", "r").readlines()

sum_of_the_priorities = 0

for lines in list_of_items_on_rucksack:

    lines = lines.strip() #lines witout \n
    size = len(lines)

    for x in set(lines[0:size//2]):#first half of lines without repeting chars
        if x in lines[size//2:]:

            if ord(x)-96 in range(1, 26+1):#for small letters
                sum_of_the_priorities += ord(x)-96

            if ord(x)-38 in range(27, 52+1):#for uppercase letters
                sum_of_the_priorities += ord(x)-38 

print(sum_of_the_priorities)