tic_toc = []
for i in range(1,10,3):
    t = [i, i+1, i+2]
    tic_toc.append(t)

def print_fun(tic_toc):
    for i in tic_toc:
        for j in i:
            print(j, end=" ")
        print()

def check_value(p,x):
    for i in range(3):
        for j in range(3):
            if x == tic_toc[i][j]:
                tic_toc[i][j] = p
    print_fun(tic_toc)

def winner(o):
    for i in range(3):
        e = s = q = r = 0
        for j in range(3):
            if tic_toc[i][j] == o:
                r += 1
            if tic_toc[j][i] == o:
                q += 1
            if i == j and tic_toc[i][j] == o:
                s += 1
            if i+j == 2 and tic_toc[i][j] == o:
                e += 1
        if r == 3 or e == 3 or q == 3 or s == 3:
            print(o + ' WINS')
            exit()

def start_game():
    for i in range(1,10):
        if i%2 == 0:
            print("X turn: Enter a valid number from 1-9")
            z = int(input())
            check_value('X',z)
        else:
            print("O turn: Enter a valid number from 1-9")
            q = int(input())
            check_value('O', q)
        if i >= 5 and i%2 == 0:
            winner('X')
        else:
            winner('O')
start_game()


