#!/usr/bin/python

class cell():
    def __init__(self, row, column, numval):
        self.column = column
        self.row = row
        self.numval = numval

    def updateNumVal(self,newNum):
        self.numval = newNum

    def boxInit(self, grid):
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

    def checkColumn(self, num, grid):
        for each in grid[self.column]:
            if num == each.getNumVal():
                return True
        return False

    def checkRow(self, num, grid):
        for each in grid:
            if num == each[self.row].getNumVal():
                return True
        return False

    def getNumVal(self):
        return self.numval

def gridInit():
    a = []
    for line in range(0,9):
        b = []
        for column in range(0,9):
            b.append(cell(line, column, 0))
        a.append(b)
    for eachline in a:
        for each in eachline:
            each.boxInit(a)
    return a

a = gridInit()

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

def printGrid(grid):
    for each in grid:
        ans = []
        for every in each:
            ans.append(every.getNumVal())
        print ans

def initCheck(grid):
    poss = []
    for each in range(9):
        b = []
        for each in range(9):
            b.append([])
        poss.append(b)
    for num in range(1,10):
        lineCount = 0
        for eachRow in grid:
            colCount = 0
            for every in eachRow:
                if num not in every.getBox() and not every.checkColumn(num, grid) and not every.checkRow(num, grid):
                    poss[lineCount][colCount].append(num)
                colCount += 1
            lineCount += 1
    return poss

printGrid(a)
print initCheck(a)[5][6]
#for each in initCheck(a):
 #   for every in each:
  #      print every

#### when complete, if len(list item) == 1, pop and insert into table
#### remove number from all list items in row and column

#### wash, rinse, repeat

#### if list item == [], ignore

#### if len(column or row length) == 8, do something
