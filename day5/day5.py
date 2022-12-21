stacks_of_marked_crates = []

input_commed = open('input_day5.txt', 'r').readlines()

def set_number_stacks(input_commed):

    for line in input_commed:
        number = 0
        if line == "\n":
            return int(x)
            break
        line = line.strip().split()
        for x in line:
            try:
                if number: 
                    if int(x) == number+1: continue
                number = int(x)
            except: break

print(set_number_stacks(input_commed))
