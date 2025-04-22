def part2():
    input = open('input.txt').readlines()
    dots = [[int(j) for j in i.strip().split(",")] for i in input if "," in i]
    fold = [i.strip().split("=") for i in input if "=" in i]
    output = []
    maxX = 0
    maxY = 0

    for f in fold:
        foldpoint = int(f[1])  
        if "y" in f[0]:
            index = 1
        else:
            index = 0
        for d in dots:
            if foldpoint < d[index]:
                d[index] = d[index]-(d[index]-foldpoint)*2

    for d in dots:
        if d not in output:
            output.append(d)
        if d[0] > maxY:
            maxY = d[0]
        if d[1] > maxX:
            maxX = d[1]
    
    for x in range(maxX+1):
        outputstring = ""
        for y in range(maxY+1):
            if [y,x] in output:
                outputstring += "#"
            else:
                outputstring += " "
        print(outputstring)

part2()