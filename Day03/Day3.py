import re

def part1():
    file = open('input.txt','r')
    common = []
    for line in file:
        splitline = [i for i in line.strip()]
        if common == []:
            common = [0 for _ in splitline]
        for i, n in enumerate(splitline):
            if n == '1':
                common[i]+=1
            else:
                common[i]-=1
    for i,n in enumerate(common):
        if n < 0:
            common[i] = 0
        else:
            common[i] = 1
    gamma = int(''.join([str(i) for i in common]),2)
    for i,n in enumerate(common):
        if n == 1:
            common[i] = 0
        else:
            common[i] = 1
    epsilon = int(''.join([str(i) for i in common]),2)
    print(gamma*epsilon)

def loop(ett, noll):
    file = [i.strip() for i in open('input.txt','r')]
    rows = len(file)
    index = 0
    rating = ''
    while len(file) > 1:
        one = 0
        zero = 0
        for i,line in enumerate(file):
            if [i for i in line.strip()][index] == '1':
                one+=1
            else:
                zero+=1
            if i == rows:
                break
        if one >= zero:
            rating += ett
        else:
            rating += noll
        index += 1
        file = [i for i in file if re.findall('^'+rating,i)]
        rows = len(file)
    return(int(file[0],2))

def part2():
    print(loop('1', '0')*loop('0', '1'))

part2()