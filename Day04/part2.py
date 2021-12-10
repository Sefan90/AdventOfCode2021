data = open("input.txt").read().split("\n")

lotto = data.pop(0).split(",")
bingo_boards = []
counter = 0
line = []

def win(win_bing, last_numb):
    summa = 0
    for i in win_bing:
        if i != "X":
            summa += int(i)
    print(summa * int(last_numb))
    exit()

for row in data:
    new_board = False
    if row == "" and new_board == False:
        new_board = True
        if counter > 0:
            bingo_boards.append(line)
            line = []
        counter += 1
        continue
    for x in row.split():
        line.append(x)
bingo_boards.append(line)

for n in lotto:
    tmp_lista = []
    for x, b in enumerate(bingo_boards):
        if n in b:
            b[b.index(n)] = "X"
            for i in range(5):
                if b[i*5] == "X" and b[i*5+1] == "X" and b[i*5+2] == "X" and b[i*5+3] == "X" and b[i*5+4] == "X":
                    tmp_lista.append(x)
                    if len(bingo_boards) == 1:
                        print(bingo_boards)
                        print(n)
                        win(bingo_boards[0], n)
                elif b[i] == "X" and b[i+5] == "X" and b[i+10] == "X" and b[i+15] == "X" and b[i+20] == "X":
                    tmp_lista.append(x)
                    if len(bingo_boards) == 1:
                        print(bingo_boards)
                        print(n)
                        win(bingo_boards[0], n)
    for t in reversed(tmp_lista):
        bingo_boards.pop(t)