import copy

stacks_of_marked_crates = []
filename = 'input_day5.txt'

input_commed = open(filename, 'r').readlines()

def set_number_stacks(input_commed):

    for number_lines,line in enumerate(input_commed):
        number_before = 0
        if line == "\n":
            return int(x),number_lines
        line = line.strip().split()
        for x in line:
            try:
                if number_before: 
                    if int(x) == number_before + 1: continue
                number_before = int(x)
            except: break

number_stacks,number_lines = set_number_stacks(input_commed)

tab = []
[tab.append([]) for i in range(number_stacks)]

for number_line in range(number_lines-2, -1, -1):
    line = input_commed[number_line]
    number_tab = 0
    space = 0
    for x in line:
        if space == 4:
            tab[number_tab].append(' ')
            space = 0
            number_tab = number_tab + 1
        if x == ' ':
            space = space + 1
            continue

        if ord(x) >= 65 and ord(x) <= 90:
            tab[number_tab].append(x)
            space = 0
            number_tab = number_tab + 1

for x in range(number_stacks):
    while(tab[x][-1] == ' '):
        if tab[x][-1] == ' ':
            tab[x].pop()

tab_part_two = copy.deepcopy(tab)

count = -1
for count, x in enumerate(open(filename, 'r')):
	pass
count += 1


for number_line in range(number_lines+1,count):
    line = input_commed[number_line].strip().split()
    Move = int(line[1])
    From = int(line[3])-1
    To = int(line[5])-1

    for i in range(Move):
        tab[To].append(tab[From][-1])
        tab[From].pop()

for x in range(number_stacks):
    print(tab[x][-1], end='')
print()
#part two

tab_help = []

for number_line in range(number_lines+1,count):
    line = input_commed[number_line].strip().split()
    Move = int(line[1])
    From = int(line[3])-1
    To = int(line[5])-1

    for i in range(Move):
        tab_help.append(tab_part_two[From][-1])
        tab_part_two[From].pop()
    for i in range(len(tab_help), 0, -1):
        tab_part_two[To].append(tab_help[i-1])
        tab_help.pop()

for x in range(number_stacks):
    print(tab_part_two[x][-1], end='')
print()