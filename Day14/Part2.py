#def rec():


def part2():
    input = open('input.txt').readlines()
    template = input[0].strip()
    rules = {i.split("->")[0].strip():i.split("->")[1].strip() for i in input if "->" in i}
    rules2 = {i.split("->")[0].strip():"" for i in input if "->" in i}
    for k in rules.keys():
        rules2[k] += rules[k[0]+rules[k]]+rules[rules[k]+k[1]]
    print(rules2)
part2()