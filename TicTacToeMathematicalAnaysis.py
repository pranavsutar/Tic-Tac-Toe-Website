# from tkinter import *
# win = Tk()
# win.title("Pranav")
# # win.iconbitmap('paintbox.ico')

# win.minsize(width=1400, height=750)
# win.maxsize(width=1800, height=1000)
# # Labels
# # l1 = 
# Nh =3
# Nv =3
# startx = 0
# starty = 0
# # ll1 = [Label(win, text = "T" + str(i), bg= "blue", fg= 'white', width = 10, height= 1) for i in range(6)]
# # ll2 = [Label(win, text = "U" + str(i), bg= "black", fg= 'white', width = 10, height= 1) for i in range(6)]
# # for i in range(6):
# #     ll1[i].place(x = 10, y = 100+25*i)
# #     ll2[i].place(x = 90, y = 100+25*i)

# lll = [[Button(win, text = "_", bg= "black", fg= 'white', width = 10, height = 2) for item in range(Nv) ] for j in range(Nh)]

# for i in range(Nh):
#     for j in range(Nv):
#         lll[i][j].place(x = startx +  80*i, y =starty + 50*j)
from math import factorial
import random

def show(ll):
    for l in ll:
        print(l)
    print()

def showw(ll):
    print(ll[0],[1,2,3], sep = '  ')
    print(ll[1],[4,5,6], sep = '  ')
    print(ll[2],[7,8,9], sep = '  ')

def transpose(a):
    return [[a[o][oo] for o in range(3)] for oo in range(3)]
def row_wise(a):
    r0 = a[0]; r1 = a[1]; r2 = a[2];
    b0 = (r0[0]==r0[1]==r0[2] and r0[0] != '_')
    b1 = (r1[0]==r1[1]==r1[2] and r1[0] != '_')
    b2 = (r2[0]==r2[1]==r2[2] and r2[0] != '_')
    return b0 or b1 or b2
def col_wise(a):
    aT = transpose(a)
    return row_wise(aT)
def diagonally(a):
    p1 = (a[0][0] == a[1][1] == a [2][2]  and a[0][0] != '_')
    p2 = (a[2][0] == a[1][1] == a [0][2]  and a[0][2] != '_')
    return p1 or p2

def check(a):
    return row_wise(a) or col_wise(a) or diagonally(a)
def whoWon(a):
    b = a[::-1][::-1]
    for i in range(3):
        b[i].replace('O','X')
    show(b)
    if(check(b)):
        return 'X'
    return 'O'
def draw(a):
    for l in a:
        if l.count('_'):
            return False
    return not check(a)

Trials = int(input('Enter Number of Trials: '))
# Trials = factorial(10)
p = [0,0,0] # X,O,Draw
for i in range(Trials):
    a = [['_' for o in range(3)] for oo in range(3)]
    # showw(a)
    nl = [1,2,3,4,5,6,7,8,9]
    for h in range(5):
        # print('\nPlayer 1\nEnter the position for the input ')
        u = random.choice(nl);x = (u-1)//3 ; y = (u+2)%3
        nl.remove(u)
 
        a[x][y] = 'X'
        # showw(a)
        if(check(a)):
            # print('Winner is Player 1 !!!\nCongratulations!!!')
            p[0] += 1
            break;
        elif(draw(a)):
            # print('The match is a Draw. Play Again.')
            p[2] += 1
            break;

        # Player 2
        # print('\nPlayer 2\nEnter the position for the input ')
        u = random.choice(nl);x = (u-1)//3 ; y = (u+2)%3
        nl.remove(u)

        a[x][y] = 'O'
        # showw(a)
        if(check(a)):
            # print('Winner is Player 2 !!!\nCongratulations!!!')
            p[1] += 1
            break;
print(p)

print('Probability of winning of Player 1 is',(p[0]*100/sum(p)).__round__(1),'%')
print('Probability of winning of Player 2 is',(p[1]*100/sum(p)).__round__(1),'%')
print('Probability of                Draw is',(p[2]*100/sum(p)).__round__(1),'%')
print('The mathematical calculations reveal that the values are 58.5%, 28.8% and 12.7% respectively')
# b = [[3*oo - o for o in range(3)] for oo in range(3)]

# show(b)
# show(transpose(b))


# for _ in range(int(input())):
#     a = [x for x in input()]
#     b = [x for x in input()]
#     c = [x for x in input()]
#     M =[a,b,c]
#     print(check(M))



