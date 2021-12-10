def part1():
    file = open('input.txt','r')
    pos = [0,0]
    for line in file:
        if 'forward' in line:
            pos[0]+=int(line.strip()[-1])
        if 'down' in line:
            pos[1]+=int(line.strip()[-1])
        if 'up' in line:
            pos[1]-=int(line.strip()[-1])
    print(pos[0]*pos[1])

def part2():
    file = open('input.txt','r')
    pos = [0,0,0]
    for line in file:
        if 'forward' in line:
            pos[0]+=int(line.strip()[-1])
            pos[1]+=pos[2]*int(line.strip()[-1])
        if 'down' in line:
            pos[2]+=int(line.strip()[-1])
        if 'up' in line:
            pos[2]-=int(line.strip()[-1])
    print(pos[0]*pos[1])

part2()