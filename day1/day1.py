list_of_calories = open("input_day1.txt", 'r').read().split('\n\n')

for i,snak in enumerate(list_of_calories):
    h_sum = 0
    for calorie in snak.split('\n'):
        if calorie:
            h_sum += int(calorie)
    list_of_calories[i] = h_sum

print(max(list_of_calories))
       
        