import re
import time
instructions = "LRRLRLRRLRRRLRLRLRRLRRRLRRRLRRLRRRLRLRLRLRLRLRLRRRLRRLRRRLLLLRRRLRLLLRRRLLRLLRRRLRRRLRLRRLRRRLRRRLLRRRLRLRRRLLRRRLRLLRRRLRRLLRLRLRLRRRLRLLRLRLRRRLRLLRLRLRRRLLRRRLRRLRRRLRLRRLRLRRLRLRRLRRRLLRRRLLLRRRLLRRLRRLRRLRLLRRLRRRLRRLRLRLRRLRRLLLRRLRLRRRLRRRLRRRLLLRLRRRLLRRRLRLLRRRR"
with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2023_12_01\day8input.txt") as file:
    list = [line.rstrip() for line in file]
map_index = {}
z_numbs = {}
for l in list:
    key = l[0]+l[1]+l[2]
    value = l[6:]
    map_index[key] = (value[1:4], value[6:9])
direction_iteration = 0
direction_index = 0
current_selection = ""
map_key = ""
ins_active = True
num_sync = True
is_zzz = False
map_key = "AAA"
count = 0
tracking_dict = {}
for key in map_index:
    if key[2] == "A":
        z_numbs[key] = (key, 0, 0)
        map_key = key
index = 0
z_check = 0
#Keep updating iterating over the smallest count until counts are the same.
print("start")
while ins_active == True:
    z_check = 0
    item_count = 0
    for d in instructions:
        if ins_active == True:
            direction_index = direction_index + 1
        cur_inst = d
        for key in z_numbs:
            if cur_inst == "R":
                z_numbs[key] = (map_index[z_numbs[key][0]][1], direction_index, 0)
            if cur_inst == "L":
                z_numbs[key] = (map_index[z_numbs[key][0]][0], direction_index, 0)
            current_selection = z_numbs[key][0]
            if current_selection[2] == "Z":
                z_numbs[key] = (z_numbs[key][0], z_numbs[key][1], 1)
                count = direction_index
            direction_iteration = direction_iteration + 1
            z_check = z_check + z_numbs[key][2]
            if z_check == 3:
                ins_active = False
            if is_zzz == True:
                ins_active = False
        print(z_numbs)
index = index + 1
print(z_numbs)
