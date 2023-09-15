input = open("/users/alfredshoukry/code/2017-advent-of-code/day-02/input.txt", "r")
total = 0
for line in input.readlines():
    int_list = [int(x) for x in line.split()]
    for i in int_list:
        for j in int_list:
            if i%j == 0 and i != j:
                total += i/j
print(total)