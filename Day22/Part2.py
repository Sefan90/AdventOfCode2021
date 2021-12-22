def getaxis(x1,x2):
    if x2 < x1:
        x1, x2 = x2, x1
    return range(x1,x2)
    
def part1():
    inputs = [i.strip().split(",") for i in open('testinput.txt').readlines()]
    cubes = {}
    for i in range(len(inputs)):
        on = False
        if "on" in inputs[i][0]:
            on = True
        for x in getaxis(int(inputs[i][0].split("=")[1].split("..")[0]),int(inputs[i][0].split("=")[1].split("..")[1])+1):
            for y in getaxis(int(inputs[i][1].split("=")[1].split("..")[0]),int(inputs[i][1].split("=")[1].split("..")[1])+1):
                for z in getaxis(int(inputs[i][2].split("=")[1].split("..")[0]),int(inputs[i][2].split("=")[1].split("..")[1])+1):
                    cubes[str(x)+","+str(y)+","+str(z)] = on
    print(sum(v == True for v in cubes.values()))
part1()
