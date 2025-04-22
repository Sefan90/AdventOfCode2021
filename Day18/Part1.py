def part1():
    input = open('input.txt').readlines()
    dots = [[int(j) for j in i.strip().split(",")] for i in input if "," in i]
    fold = [i.strip().split("=") for i in input if "=" in i]
    output = []

    f = fold[0]
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
    print(len(output))
part1()