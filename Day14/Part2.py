import copy
data = open("input.txt").read().split("\n")

dct = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in data if "->" in line}
sum_dct = {line.split(" -> ")[0]:0 for line in data if "->" in line}
word = data[0]
last = word[-1]
checklist = list(set(line.split("-> ")[1] for line in data if "->" in line))

for k in dct:
    if k in word:
        sum_dct[k] += 1

for i in range(40):
    tmp_dct = copy.deepcopy(sum_dct)
    for k, v in dct.items():
        tmp = sum_dct.get(k)
        if tmp > 0:
            tmp_dct[k[0] + v] += tmp
            tmp_dct[v + k[1]] += tmp
            tmp_dct[k] -= tmp
    sum_dct = tmp_dct   

sum_list = list(set(line.split(" -> ")[1] for line in data if "->" in line))
resultat_lista = []
for x in sum_list:
    tmp_sum = 0
    for k, v in sum_dct.items():
        if x in k[0]:
            tmp_sum += v
    if last == x:
        tmp_sum += 1
    resultat_lista.append(tmp_sum)
print(max(resultat_lista) - min(resultat_lista))