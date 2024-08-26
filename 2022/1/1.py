class calories:

    calorie_list = []
    total_list = []

    def __init__(self, calorie_input):
        if calorie_input == "":
            calorie_input = 0
            calories.total_list.append(sum(calories.calorie_list))
            print(calories.total_list)
            calories.calorie_list.clear() 
            pass
        else:
            self.calorie_input = calorie_input
            calories.calorie_list.append(int(self.calorie_input))
        
    def find_highest ():
        calories.total_list.sort()
        return calories.total_list[-1]

    def find_top3():
        calories.total_list.sort()
        return calories.total_list[-3:]


if __name__ == '__main__':
    with open(r"C:\Users\soren.peterson\Desktop\Tempshapes\2024_08_26\AOC\1\input.txt") as file:
        list = [line.rstrip() for line in file]
    for i in list:
        calories(i)
    top1 = calories.find_highest()
    top3 = calories.find_top3()
    print(top1)
    print(sum(top3))
