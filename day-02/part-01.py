input = open("/Users/alfredshoukry/code/2017-advent-of-code/day-02/input.txt", "r")
total = 0
for line in input.readlines():
    int_list = [int(x) for x in line.split()]
    maximum = max(int_list)
    minimum = min(int_list)
    total = total + maximum - minimum
print(total)