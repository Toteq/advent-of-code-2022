big_list = open('input_day4.txt', 'r').readlines()

sum_pairs_does_one_range_fully_contain_the_other = 0
first_tab = []
second_tab = []

how_many_assignment_pairs_do_the_ranges_overlap = 0 #part two

for line in big_list:
    line = line.strip().split(",")#lines without \n and divided into elves

    for x in range(2):
        diver = line[x].find("-")
        first = int(line[x][0:diver])
        second = int(line[x][diver+1:len(line[x])])+1

        {first_tab.append(index) for index in range(first,second) if x == 0}
        {second_tab.append(index) for index in range(first,second) if x == 1}

    if len(first_tab) > len(second_tab):
        if set(first_tab).intersection(set(second_tab)) == set(second_tab): sum_pairs_does_one_range_fully_contain_the_other += 1
        if set(second_tab).intersection(set(first_tab)): how_many_assignment_pairs_do_the_ranges_overlap += 1
        first_tab = []
        second_tab = []
    else:
        if set(second_tab).intersection(set(first_tab)) == set(first_tab): sum_pairs_does_one_range_fully_contain_the_other += 1
        if set(first_tab).intersection(set(second_tab)): how_many_assignment_pairs_do_the_ranges_overlap += 1
        first_tab = []
        second_tab = []

print(sum_pairs_does_one_range_fully_contain_the_other)
print(how_many_assignment_pairs_do_the_ranges_overlap)