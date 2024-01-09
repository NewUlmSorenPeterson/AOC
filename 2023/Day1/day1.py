import re
list = []
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2023_12_01\day1input.txt") as file:
    list = [line.rstrip() for line in file]
full_list = []
temp_wordlist = {}
temp_list = []
index_shift = 0
for i in list:
    print(i) 
    for key in help_dict:
        if key in i:
            word_index = [m.start() for m in re.finditer(key, i)]
            for k in word_index:
                temp_wordlist[k] = help_dict[key]
    ordered_temp = dict(sorted(temp_wordlist.items()))
    index_it = 0
    for key in ordered_temp:
        i = i[ : int(key) + int(index_it)] + ordered_temp[key] + i[int(key) + int(index_it) : ]
        index_it = index_it + 1
    temp_wordlist.clear()
    print(i)   
    for t in i:
        if t.isdigit() == True:
            number = t
            temp_list.append(t)
    last = temp_list[-1]
    first = temp_list[0]
    value = first + last
    temp_list.clear()
    full_list.append(int(value))
    print(value)
print(sum(full_list))
        