def findcave(path,caves):
    output = []
    for i in caves:
        if i[0] == path[-1] and i[1] != "start":
            if i[1] == "end":
                output.append(path+[i[1]])
            elif (i[1].islower() == True and path.count(i[1]) < 2) or i[1].isupper() == True:
                tmp = path+[i[1]]
                if [tmp.count(x) > 1 for x in tmp if x.islower() == True].count(True) <= 2:
                    output += findcave(tmp,caves)
        else:
            output.append(path)
    return output   

def part2():
    caves = [[j for j in i.strip().split("-")] for i in open('input.txt').readlines()]
    for i in reversed(caves):
        caves.append([i[1],i[0]])
    print(caves)
    output = []
    for i in findcave(["start"],caves):
        if i[-1] == "end" and i not in output:
            output.append(i)
    print(len(output))
    
part2()