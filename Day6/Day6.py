def part1():
    fish = [int(i) for i in open('input.txt').readline().split(",")]
    for _ in range(80):
        for i in reversed(range(len(fish))):
            fish[i] -= 1
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)
    print(len(fish))

def part2():
    fish = [int(i) for i in open('input.txt').readline().split(",")]
    days = [0 for _ in range(7)]
    for i in fish:
        days[i] += 1
    toadd = [0,0]
    rangeend = 257
    for i in range(1,rangeend):
        index = i%7
        tmpadd = days[index]
        days[index] += toadd[0]
        toadd[0] = toadd[1]
        toadd[1] = tmpadd
    days[(rangeend)%7] += toadd[0]
    print(sum(days))

part2()