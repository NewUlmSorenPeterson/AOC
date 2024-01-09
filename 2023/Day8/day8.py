import re
import time
instructions = "LRRLRLRRLRRRLRLRLRRLRRRLRRRLRRLRRRLRLRLRLRLRLRLRRRLRRLRRRLLLLRRRLRLLLRRRLLRLLRRRLRRRLRLRRLRRRLRRRLLRRRLRLRRRLLRRRLRLLRRRLRRLLRLRLRLRRRLRLLRLRLRRRLRLLRLRLRRRLLRRRLRRLRRRLRLRRLRLRRLRLRRLRRRLLRRRLLLRRRLLRRLRRLRRLRLLRRLRRRLRRLRLRLRRLRRLLLRRLRLRRRLRRRLRRRLLLRLRRRLLRRRLRLLRRRR"
with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2023_12_01\day8input.txt") as file:
    list = [line.rstrip() for line in file]
map_index = {
}
for l in list:
    key = l[0]+l[1]+l[2]
    value = l[6:]
    map_index[key] = (value[1:4], value[6:9])
print(map_index)
direction_iteration = 1
direction_index = 1
current_selection = ""
map_key = ""
ins_active = True
is_zzz = False
map_key = "AAA"
while ins_active == True:
    print(direction_iteration)
    for d in instructions:
        if d == "R":
            current_selection = map_index[map_key][1]
        if d == "L":
            current_selection = map_index[map_key][0]
        map_key = current_selection
        print(current_selection)
        if "ZZZ" in current_selection:
            ins_active == False
            is_zzz = True
            count = direction_index
        if ins_active == True:
            direction_index = direction_index + 1
    direction_iteration = direction_iteration + 1
    if is_zzz == True:
        ins_active = False
    if direction_iteration > 1000:
        ins_active = False
print(direction_index)
print(direction_iteration)
print(count)