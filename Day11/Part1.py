def part1():
    input = open('input.txt').readlines()
    rows = [[int(j) for j in i.strip()] for i in input]
    flashlist = [[False for _ in i.strip()] for i in input]
    flashes = 0
    flashing = True
    for p in range(100):
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
        print("")
        for r in rows:
            print(r)
    print(flashes)

part1()