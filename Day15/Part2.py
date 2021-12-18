map = [[int(j) for j in i.strip()]for i in open('input.txt').readlines()]
minimum = 0

def rec(x,y, count):
    global minimum
    if minimum != 0 and minimum < count:
            return -1
    if x == len(map)-1 and y == len(map[0])-1:
        if minimum == 0 or minimum > count:
            minimum = count
        return count
    if x < len(map)-1 and y < len(map[0])-1:
        return [rec(x+1,y,count+map[x+1][y]),rec(x,y+1,count+map[x][y+1])]
    elif x < len(map)-1:
        return rec(x+1,y,count+map[x+1][y])
    elif y < len(map[0])-1:
        return rec(x,y+1,count+map[x][y+1])

def part1():
    rec(0,0,0)
    print(minimum)

part1()
#531 high