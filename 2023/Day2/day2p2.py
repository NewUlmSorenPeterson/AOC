import re

with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2023_12_01\day2input.txt") as file:
    list = [line.rstrip() for line in file]
tlist = ['Game 1: 2 green, 12 blue; 6 red, 6 blue; 8 blue, 5 green, 5 red; 5 green, 13 blue; 3 green, 7 red, 10 blue; 13 blue, 8 red']
game_counter = 0
id = 0
power_sum = 0
for l in list:
    game_dict = {
                'green' : [],
                'red' : [],
                'blue' : [] 
                }
    id = id + 1
    red_list = []
    blue_list = []
    green_list = []
    string1 = re.sub(r'^.*?:', ':', l)
    string2 = string1.replace(':', '')
    gameindex = [m.start() for m in re.finditer(';', string2)]
    game_list = re.split('[;:]', string2)
    game_fail = False
    for g in game_list:
        rolls = re.split('[,:]', g)
        rolls = [x.strip(' ') for x in rolls]
        for r in rolls:
            rolls2 = re.split('[ :]', r)
            game_dict[rolls2[1]].append(rolls2[0])
    power = 1
    for key in game_dict:
        res = [eval(i) for i in game_dict[key]]
        a,i = max((a,i) for (i,a) in enumerate(res))
        print("{} highest number: {}".format(key, a))
        power = power * a
    power_sum = power_sum + power
    print(power_sum)
