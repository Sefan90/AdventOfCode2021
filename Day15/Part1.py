map = [[int(j) for j in i.strip()]for i in open('input.txt').readlines()]

def search(coords):
    counter = []
    while coords != [len(map)-1,len(map[0])-1]:
        if coords[0]+1 < len(map) and coords[1]+1 < len(map[0]):
            if map[coords[0]+1][coords[1]] < map[coords[0]][coords[1]+1]:
                coords[0]+=1
            else:
                coords[1]+=1
        elif coords[0]+1 < len(map):
            coords[0]+=1
        elif coords[1]+1 < len(map[0]):
            coords[1]+=1
        counter.append(map[coords[0]][coords[1]])
    return sum(counter)

minimum = search([0,0])
def rec(x,y, count):
    global minimum
    if minimum != 0 and minimum <= count:
        return
    elif x == len(map)-1 and y == len(map[0])-1:
        if minimum == 0 or minimum > count:
            minimum = count
            print(minimum)
    elif x < len(map)-1 and y < len(map[0])-1:
        rec(x+1,y,count+map[x+1][y])
        rec(x,y+1,count+map[x][y+1])
    elif x < len(map)-1:
        rec(x+1,y,count+map[x+1][y])
    elif y < len(map[0])-1:
        rec(x,y+1,count+map[x][y+1])

def part1():
    rec(0,0,0)
    print(minimum)


part1()
#531 high