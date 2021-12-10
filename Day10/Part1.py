def part1():
    chunks = [i.strip() for i in open('input.txt').readlines()]
    mapper = {"(":")","[":"]","{":"}","<":">"}
    starters = []
    output = 0
    for row in chunks:
        for c in row:
            if c in mapper.keys():
                starters.append(c)
            elif c in mapper.values():
                if len(starters) > 0:
                    if mapper[starters[-1]] == c:
                        del starters[-1]
                    else:
                        starters = []
                        if c == ")":
                            output += 3
                        elif c == "]":
                            output += 57
                        elif c == "}":
                            output += 1197
                        elif c == ">":
                            output += 25137

    print(output)

part1()