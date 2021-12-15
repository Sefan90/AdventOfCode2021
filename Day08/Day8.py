import statistics

def part1():
    signals = [i.strip().split("|") for i in open('input.txt').readlines()]
    output = 0
    for s in signals:
        for i in s[1].split(" "):
            if len(i) in [2,4,3,7]:
                output += 1
    print(output)

def part2():
    signals = [i.strip().split("|") for i in open('input.txt').readlines()]
    output = 0
    numbers = ["" for _ in range(10)]
    segments = ["" for _ in range(7)]
    five = []
    six = []
    for s in signals:
        for i in s[0].split(" "):
            if len(i) == 2:
                numbers[1] = sorted(i)
            elif len(i) == 4:
                numbers[4] = sorted(i)
            elif len(i) == 3:
                numbers[7] = sorted(i)
            elif len(i) == 7:
                numbers[8] = sorted(i)
            elif len(i) == 5:
                five.append(sorted(i))
            elif len(i) == 6:
                six.append(sorted(i))

        segments[0] = [n for n in numbers[7] if n not in numbers[1]][0]
        for f in five:
            tmp = ""
            for n in f:
                if n not in numbers[4] and n not in segments[0]:
                    tmp += n
            if len(tmp) == 1:
                segments[6] = tmp
        segments[4] = [n for n in numbers[8] if n not in numbers[4] and n not in numbers[7] and n not in segments[6]][0]
        for f in six:
            tmp = ""
            for n in f:
                if n not in numbers[7] and n in numbers[4]:
                    tmp += n
            if len(tmp) == 1:        
                segments[1] = tmp
        segments[3] = [n for n in numbers[4] if n not in numbers[7] and n not in segments[1]][0]
        for f in six:
            tmp = ""
            for n in numbers[1]:
                if n not in f:
                    tmp += n
            if len(tmp) == 1:    
                segments[2] = tmp
        segments[5] = [n for n in numbers[4] if n in numbers[1] and n in numbers[7] and n not in segments[2]][0]

        resultat = ""
        for i in s[1].split(" "):
            if len(i) == 2:
                resultat += "1"
            elif len(i) == 4:
                resultat += "4"
            elif len(i) == 3:
                resultat += "7"
            elif len(i) == 7:
                resultat += "8"
            elif len(i) == 5:
                if segments[1] not in i and segments[5] not in i:
                    resultat += "2"
                elif segments[1] not in i and segments[4] not in i:
                    resultat += "3"
                else:
                    resultat += "5"
            elif len(i) == 6:
                if segments[3] not in i:
                    resultat += "0"
                elif segments[2] not in i:
                    resultat += "6"
                else:
                    resultat += "9"
        output += int(resultat)
    print(output)

part2()
