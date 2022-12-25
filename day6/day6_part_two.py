filename = 'input_day6.txt'
datastream_buffer = open(filename, 'r').read()

help_list = []

for i in range(len(datastream_buffer)-14):

    for x in range(14):
        help_list.append(datastream_buffer[i+x])

    len_list = len(help_list)
    len_set = len(set(help_list))

    if len_list == len_set:
        print(i+14)
        break
    else:
        help_list = []
