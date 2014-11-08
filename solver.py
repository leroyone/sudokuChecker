#!/usr/bin/python

class cell():
    def __init__(self, row, column, numval):
        self.column = column
        self.row = row
        self.numval = numval

    def updateNumVal(self,newNum):
        self.numval = newNum

    def boxInit(self,grid):
        a = []
        x = (self.row / 3)*3
        y = (self.column / 3)*3
        for rownum in range(x, x+3):
            for colnum in range(y, y+3):
                a.append(grid[rownum][colnum])
        self.box = a

    def getBox(self):
        a = []
        for each in self.box:
            a.append(each.getNumVal())
        return a

    def getNumVal(self):
        return self.numval



a = []

for line in range(0,9):
    b = []
    for column in range(0,9):
        b.append(cell(line, column, 0))
    a.append(b)

for eachline in a:
    for each in eachline:
        each.boxInit(a)

###### maker #####

a[0][6].updateNumVal(5)
a[0][7].updateNumVal(2)
a[1][3].updateNumVal(5)
a[1][4].updateNumVal(3)
a[2][1].updateNumVal(3)
a[2][3].updateNumVal(4)
a[2][4].updateNumVal(7)
a[3][0].updateNumVal(1)
a[3][1].updateNumVal(4)
a[3][6].updateNumVal(2)
a[4][2].updateNumVal(7)
a[4][3].updateNumVal(1)
a[4][5].updateNumVal(5)
a[4][6].updateNumVal(6)
a[5][2].updateNumVal(2)
a[5][7].updateNumVal(7)
a[5][8].updateNumVal(5)
a[6][4].updateNumVal(4)
a[6][5].updateNumVal(3)
a[6][7].updateNumVal(8)
a[7][4].updateNumVal(6)
a[7][5].updateNumVal(7)
a[8][1].updateNumVal(6)
a[8][2].updateNumVal(8)

##############
''' 
for each in a:
    ans = []
    for every in each:
        ans.append(every.getNumVal())
    print ans

#### check if number not in column or row
def initcheck(grid):
    pass
'''

#### if not, add to list

#### when complete, if len(list item) == 1, pop and insert into table
#### remove number from all list items in row and column

#### wash, rinse, repeat

#### if list item == [], ignore

#### list items in dict?
#### list of list items?

#### do something about box!!
#### classes?? for each cell, containing column, row and box

#### if len(column or row length) == 8, do something
''' 
def checkColumn(num, col):
    if num in a[col]:
        return True
    else:
        return False

def checkRow(num, row):
    for each in a:
        if num == each[row]:
            return True
    return False

def checkBox():
    pass

print checkColumn(2,0)
print checkRow(2,5)
'''

print a[0][7].getNumVal()
print a[0][7].getBox()
