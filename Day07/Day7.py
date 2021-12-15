import statistics

def part1():
    crabs = [int(i) for i in open('input.txt').readline().split(",")]
    print(int(sum([abs(i-statistics.median(crabs)) for i in crabs])))

def part2():
    crabs = [int(i) for i in open('input.txt').readline().split(",")]
    print(min([sum([sum([s for s in range(abs(max([c,i])-min([c,i])+1))]) for c in crabs]) for i in range(min(crabs),max(crabs)+1)]))

def part12():
    crabs = [int(i) for i in open('input.txt').readline().split(",")]
    mean = int(statistics.mean(crabs))
    base = sum([sum([s for s in range(abs(max([c,mean])-min([c,mean])+1))]) for c in crabs])
    print(base)
    if base > sum([sum([s for s in range(abs(max([c,mean+1])-min([c,mean+1])+1))]) for c in crabs]):
        while True:
            if base > sum([sum([s for s in range(abs(max([c,mean+1])-min([c,mean+1])+1))]) for c in crabs]):
                mean += 1
                base = sum([sum([s for s in range(abs(max([c,mean])-min([c,mean])+1))]) for c in crabs])
            else:
                break
    elif base > sum([sum([s for s in range(abs(max([c,mean-1])-min([c,mean-1])+1))]) for c in crabs]):
        while True:
            if base > sum([sum([s for s in range(abs(max([c,mean-1])-min([c,mean-1])+1))]) for c in crabs]):
                mean -= 1
                base = sum([sum([s for s in range(abs(max([c,mean])-min([c,mean])+1))]) for c in crabs])
            else:
                break
    print(base)

part12()
