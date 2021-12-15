def findcave(path,caves):
    output = []
    for i in caves:
        if i[0] == path[-1]:
            if i[1] == "end":
                output.append(path+[i[1]])
            elif (i[1].islower() == True and i[1] not in path) or i[1].isupper() == True:
                output += findcave(path+[i[1]],caves)
        else:
            output.append(path)
    return output

def part1():
    caves = [[j for j in i.strip().split("-")] for i in open('input.txt').readlines()]
    for i in reversed(caves):
        caves.append([i[1],i[0]])
    output = []
    for i in findcave(["start"],caves):
        if i[-1] == "end" and i not in output:
            output.append(i)
    print(len(output))
    
part1()