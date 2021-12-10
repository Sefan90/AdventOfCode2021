def part2():
    chunks = [i.strip() for i in open('input.txt').readlines()]
    mapper = {"(":")","[":"]","{":"}","<":">"}
    starters = []
    output = []
    for row in chunks:
        skip = False
        for c in row:
            if c in mapper.keys():
                starters.append(c)
            elif c in mapper.values():
                if len(starters) > 0:
                    if mapper[starters[-1]] == c:
                        del starters[-1]
                    else:
                        skip = True
        if skip == False:
            out = 0
            for s in reversed(starters):
                out *= 5
                if s == "(":
                    out += 1
                elif s == "[":
                    out += 2
                elif s == "{":
                    out += 3
                elif s == "<":
                    out += 4
            output.append(out)
        starters = []

    print(sorted(output)[len(output)//2])

part2()