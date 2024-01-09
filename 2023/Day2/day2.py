import re

with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2023_12_01\day2input.txt") as file:
    list = [line.rstrip() for line in file]
tlist = ['Game 1: 2 green, 12 blue; 6 red, 6 blue; 8 blue, 5 green, 5 red; 5 green, 13 blue; 3 green, 7 red, 10 blue; 13 blue, 8 red']
game_counter = 0
id = 0
for l in list:
    id = id + 1
    string1 = re.sub(r'^.*?:', ':', l)
    string2 = string1.replace(':', '')
    gameindex = [m.start() for m in re.finditer(';', string2)]
    game_list = re.split('[;:]', string2)
    game_fail = False
    for g in game_list:
        game_dict = {
        'green' : 0,
        'red' : 0,
        'blue' : 0 
        }
        rolls = re.split('[,:]', g)
        rolls = [x.strip(' ') for x in rolls]
        for r in rolls:
            rolls2 = re.split('[ :]', r)
            game_dict[rolls2[1]] = game_dict[rolls2[1]] + int(rolls2[0])
            print(game_dict)
        if game_dict['green'] > 13:
            game_fail = True
        if game_dict['red'] > 12:
            game_fail = True
        if game_dict['blue'] > 14:
            game_fail = True
    if game_fail == False:
        game_counter = game_counter + id
    print(game_dict)
    print(id)
    print(game_fail)
    print(game_counter)
print(game_counter)