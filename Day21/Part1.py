def part1():
    players = [int(i.strip().split(": ")[1]) for i in open('input.txt').readlines()]
    score = [0,0]
    dice = 1
    rolls = 0
    loop = True

    while loop:
        for i in range(2):
            tmp = (players[i]+dice*3+1+2)%10
            if tmp == 0: 
                tmp = 10
            players[i] = tmp
            score[i] += players[i]
            dice += 3
            rolls += 3
            if score[i] >= 1000:
                loop = False
                break
    print(rolls*min(score[0],score[1]))

part1()
