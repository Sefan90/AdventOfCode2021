import statistics

def part1():
    heightmap = [[int(j) for j in i.strip()] for i in open('input.txt').readlines()]
    output = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            test = True
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                     if y+i >= 0 and x+j >= 0 and y+i < len(heightmap) and x+j < len(heightmap[y]):
                        if heightmap[y][x] >= heightmap[y+i][x+j] and ((i == 0 and j in [-1,1]) or (i in [1,-1] and j == 0)):
                            test = False
            if test == True:
                output += heightmap[y][x] + 1
    print(output)

def part2():
    heightmap = [[int(j) for j in i.strip()] for i in open('input.txt').readlines()]
    lowpoints = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            test = True
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                     if y+i >= 0 and x+j >= 0 and y+i < len(heightmap) and x+j < len(heightmap[y]):
                        if heightmap[y][x] >= heightmap[y+i][x+j] and ((i == 0 and j in [-1,1]) or (i in [1,-1] and j == 0)):
                            test = False
            if test == True:
                lowpoints.append([y,x])
    basin = []
    for i in lowpoints:
        points = [i]
        while True:
            tmp_points = []
            for p in points:
                y = p[0]
                x = p[1]
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if y+i >= 0 and x+j >= 0 and y+i < len(heightmap) and x+j < len(heightmap[y]):
                            if heightmap[y+i][x+j] != 9 and ((i == 0 and j in [-1,1]) or (i in [1,-1] and j == 0)):
                                tmp_points.append([y+i,x+j])
            if len([item for item in tmp_points if item not in points]) == 0:
                basin.append(points)
                break

            for p in tmp_points:
                if p not in points:
                    points += [p]
    max_basin = []
    for b in basin:
        max_basin.append(len(b))
    print(sorted(max_basin)[-1]*sorted(max_basin)[-2]*sorted(max_basin)[-3])

part2()