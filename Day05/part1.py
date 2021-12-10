
def part1():
    data = [i.split(" -> ") for i in open("input.txt").read().split("\n")]
    lines = []
    for line in data:
        x1 = int(line[0].split(",")[0])
        y1 = int(line[0].split(",")[1])
        x2 = int(line[1].split(",")[0])
        y2 = int(line[1].split(",")[1])
        if x1 == x2:
            if y1 < y2:
                lines.append(set(str(x1)+","+str(i) for i in range(y1,y2+1)))
            else:
                lines.append(set(str(x1)+","+str(i) for i in range(y2,y1+1)))
        elif y2 == y1:
            if x1 < x2:
                lines.append(set(str(i)+","+str(y1) for i in range(x1,x2+1)))
            else:
                lines.append(set(str(i)+","+str(y1) for i in range(x2,x1+1)))
    
    output = set()
    for i, line in enumerate(lines):
        for j, line2 in enumerate(lines):
            if j == i:
                continue
            else:
                output |= line&line2
    print(len(output))
 