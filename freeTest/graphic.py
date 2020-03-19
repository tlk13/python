from tkinter import *
from tkinter import messagebox as mb


import time

def evaluate(list):
    solution = list
    if not validFirst(list):
        fault()
    else:
        z = zeroes(list)
        (solution,sol) = backtrack(list,z, len(z), 0)
    return solution

#backtrack algorithm
def backtrack(list, zers, zerslen, n):
    if n == zerslen:  return (list, 2)
    (x,y) = zers[n]
    nlist = list

    for z in range(1,10):
        nlist[y][x] = z
        if valid (nlist, (x,y), z):
            (nnlist, sol) = backtrack(nlist, zers, zerslen, n+1)
            if(sol) == 2:
                return (nnlist,2)
        nlist[y][x] = 0
    return (list, 0)

#findsAllZeroes
def zeroes(list):
    zers = []
    for x in range(9):
        for y in range(9):
            if list[y][x] ==0:
                zers.append((x,y))
    return zers

#check indiviudal cell
def valid(list, tupl, change):
    (x,y) = tupl

    if change in (list[y][:(x)]+list[y][(x+1):]):
        return False

    lina = [i[x] for i in list]
    if change in (lina[:y]+lina[(y+1):]):
        return False

    bx = x // 3
    by = y // 3
    pos = x%3+3*(y%3)
    line = []
    for s in range(3):
        for t in range(3):
            line.append(list[s+3*by][t+3*bx])
    if change in (line[:pos]+line[(pos+1):]):
        return False
    return True

#check if combination is valid:
def validFirst(list):
    for x in range(9):
        if not lineValid(list[x]): return False
        if not lineValid([i[x] for i in list ]): return False
    for x in range(3):
        for y in range(3):
            line = []
            for s in range(3):
                for t in range(3):
                    line.append(list[s+3*y][t+3*x])
            if not lineValid(line): return False
    return True


def lineValid(line):
    l = [i for i in line if i != 0]
    return len(l) == len(set(l))


#methods for handling GUI to information

def fault(): mb.showerror("Error", "Sorry, there seems to be something wrong about your inputs for the SUDOKU")

def clicked():
    list = []
    for x in range(9):
        list.append([])
        for y in range(9):
            num = l[x][y].get()
            if num == '': num =0
            try:
                number = int(num)
                if number // 10 == 0:
                    list[x].append(number)
                else:
                    fault()
                    return
            except:
                print("Specific error")
                fault()
                return

    for li in list: print(li)
    solution = evaluate(list)
    display(solution)

def display(solution):
    for x in range(9):
        for y in range(9):
            l[x][y].delete(0, END)
            l[x][y].insert(0, solution[x][y])

#setup

root = Tk()
l = []
for x in range(9):
    ll = []
    for y in range(9):
        e = Entry(root, width=3)
        e.grid(row=x, column = y)
        ll.append(e)
    l.append(ll)

b = Button(root, text="Solve", command=clicked)
b.grid(row=10, columnspan =9)



mainloop()
