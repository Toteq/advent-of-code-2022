list_of_items_on_rucksack = open("input_day3.txt", "r").readlines()

sum_of_the_priorities = 0

i = 0

while(i<(len(list_of_items_on_rucksack)//3)):

    rucksack_one = list_of_items_on_rucksack[i*3].strip()
    rucksack_two = list_of_items_on_rucksack[(i*3)+1].strip()
    rucksack_three = list_of_items_on_rucksack[(i*3)+2].strip()

    for x in set(rucksack_one): #first rucksack letters without repeting
        if x in rucksack_two and x in rucksack_three:
            
            if ord(x)-96 in range(1, 26+1):#for lowercase letters
                sum_of_the_priorities += ord(x)-96

            if ord(x)-38 in range(27, 52+1):#for uppercase letters
                sum_of_the_priorities += ord(x)-38

            break

    i += 1

print(sum_of_the_priorities)