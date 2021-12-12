def part1():
    input = open('input.txt').readlines()
    rows = [[int(j) for j in i.strip()] for i in input]
    flashlist = [[False for _ in i.strip()] for i in input]
    inputlen = len(rows)*len(rows[0])
    flashing = True
    counter = 0
    while True:
        counter += 1
        flashes = 0
        for i, r in enumerate(rows):
            for j, l in enumerate(r):
                rows[i][j] += 1
        
        flashing = True
        while flashing == True:
            flashing = False
            flashlist = [[False for _ in c.strip()] for c in input]
            
            for i, r in enumerate(rows):
                for j, l in enumerate(r):
                    if rows[i][j] > 9 and flashlist[i][j] == False:
                        flashing = True
                        flashlist[i][j] = True
                        rows[i][j] = 0
                        flashes += 1
                        for x in [-1,0,1]:
                            for y in [-1,0,1]:
                                if i + x >= 0 and j + y >= 0 and i + x < len(rows) and j + y < len(r) and rows[i + x][j + y] != 0:
                                    rows[i + x][j + y] += 1
        if flashes == inputlen:
            print(counter)
            break

part1()