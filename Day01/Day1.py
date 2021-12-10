def part1():
    file = open('input.txt','r')
    counter = -1
    last = 0
    for line in file:
        if int(line) > last:
            counter+=1
        last = int(line)
    print(counter)

def part2():
    file = open('input.txt','r')
    counter = 0
    window = 0
    last = [0,0,0,0]
    for line in file:
        last.append(int(line))
        last.pop(0)
        if window == 3:
            if sum(last[0:3]) < sum(last[1:4]):
                counter+=1
        else:
            window+=1
    print(counter)

part2()