def part1():
    input = open('input.txt').readlines()
    template = input[0].strip()
    rules = {i.split("->")[0].strip():i.split("->")[1].strip() for i in input if "->" in i}
    for _ in range(10):
        temp = ""
        for i in range(len(template)-1):
            temp += template[i]
            temp += rules.get(template[i]+template[i+1])
        template = temp + template[-1]
    counter = {i:0 for i in set(rules.values())}
    for k in counter.keys():
        counter[k] = template.count(k)
    print(max(counter.values())-min(counter.values()))

part1()