output = [0,0]

def rec(players,score):
    if score[0] >= 21:
        output[0] += 1
        return
    elif score[1] >= 21:
        output[1] += 1
        return
    for i in range(3,10):
        tmp = (players[0]+i)%10
        if tmp == 0: 
            tmp = 10
        for j in range(3,10):
            tmp2 = (players[1]+j)%10
            if tmp2 == 0: 
                tmp2 = 10
            rec([tmp,tmp2],[score[0]+tmp,score[1]+tmp2])

def part2():
    players = [int(i.strip().split(": ")[1]) for i in open('testinput.txt').readlines()]
    score = [0,0]
    rec(players,score)
    print(output)

part2()