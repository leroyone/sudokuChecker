#!/usr/bin/python -B

class cell():
    POSS = None

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

def printGrid(grid):
    for each in grid:
        ans = []
        for every in each:
            ans.append(every.getNumVal())
        print ans

def makePoss(grid):
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
                if every.getNumVal() == 0 and num not in every.getBox() and not every.checkColumn(num, grid) and not every.checkRow(num, grid):
                    poss[lineCount][colCount].append(num)
                colCount += 1
            lineCount += 1
    cell.POSS = poss

def checkPoss(grid):
    test = True
    while test == True:
        test = False
        rowCount = 0
        for each in cell.POSS:
            colCount = 0
            for every in each:
                if len(every) == 1:
                    test = True
                    grid[rowCount][colCount].updateNumVal(every.pop())
                colCount += 1
            rowCount += 1
        if test == True:
            makePoss(grid)

def basicRowFind(num, gridRow, grid):
    a = [[]]
    for aBox in range(3):
        theBox = grid[gridRow*3][aBox*3].getBox()
        a[0].append(num in theBox)
        a.append(theBox)
    if sum(a[0]) == 2:
        ### check remaining box for 2 of 3 (update grid and poss)
        boxToCheck = a[0].index(False)
        goodBoxes = [0,1,2]
        goodBoxes.remove(boxToCheck)
        x = [0,1,2]
        a.pop(0)
        for each in goodBoxes:
            x.remove((a[each].index(num))/3)
        x = x[0]
        rowToCheck = a[boxToCheck][x*3:x*3+3]
        if rowToCheck.count(0) == 1:
            grid[gridRow*3+x][boxToCheck*3+rowToCheck.index(0)].updateNumVal(num)
            makePoss(grid)
            return
            ### if not
            ### check poss (update grid and poss)
                ### maybe if not, check adjacent or return fail message?

def basicColFind(num, gridCol, grid):
    a = [[]]
    for aBox in range(3):
        theBox = grid[aBox*3][gridCol*3].getBox()
        a[0].append(num in theBox)
        a.append(theBox)
    if sum(a[0]) == 2:
        pass
        ### check remaining box for 2 of 3 (update grid and poss)
            ### if not
            ### check poss (update grid and poss)
                ### maybe if not, check adjacent or return fail message?


def basicNextStep(num, grid):
    pass

#### make change checker

def loopit(grid):
    for eachNum in range(1,10):
        for eachRow in range(3):
            basicRowFind(eachNum,eachRow,grid)

#### setup a sample puzzle ####
a = gridInit()
import examples
examples.example1(a)
makePoss(a)
printGrid(a)
loopit(a)
print
printGrid(a)
###############################

#### when complete, if len(list item) == 1, pop and insert into table
#### remove number from all list items in row and column

#### wash, rinse, repeat

#### if list item == [], ignore

#### if len(column or row length) == 8, do something
