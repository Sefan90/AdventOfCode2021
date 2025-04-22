def part1():
    data = open('input.txt').readlines()
    map = [[int(j) for j in i.strip()]for i in data]
    visited = [[False for _ in i.strip()]for i in data]
    map[0][0] = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if x == 0 and y == 0:
                continue
            elif x == 0:
                map[x][y] += map[x][y-1]
            elif y == 0:
                map[x][y] += map[x-1][y]
            else:
                map[x][y] += min(map[x-1][y],map[x][y-1])
    for m in map:
        print(m)
    print(map[len(map)-1][len(map[0])-1])

def part2():
    data = open('input.txt').readlines()
    map = [[int(j) for j in i.strip()]for i in data]
    visited = [[False for _ in i.strip()]for i in data]
    map[0][0] = 0
    for x in reversed(range(len(map))):
        for y in reversed(range(len(map[0]))):
            if x == len(map)-1 and y == len(map[0])-1:
                continue
            elif x == len(map)-1:
                map[x][y] += map[x][y+1]
            elif y == len(map[0])-1:
                map[x][y] += map[x+1][y]
            else:
                map[x][y] += min(map[x+1][y],map[x][y+1])
    for m in map:
        print(m)
    print(map[0][0])

part1()