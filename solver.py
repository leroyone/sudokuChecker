#!/usr/bin/python -B

class cell():
    POSS = None

    def __init__(self, row, col, numval):
        self.col = col
        self.row = row
        self.numval = numval

    def updateNumVal(self, newNum):
        self.numval = newNum

    def boxInit(self, grid):
        a = []
        x = (self.row / 3)*3
        y = (self.col / 3)*3
        for rownum in range(x, x+3):
            for colnum in range(y, y+3):
                a.append(grid[rownum][colnum])
        self.box = a

    def getRawBox(self):
        return self.box

    def colInit(self, grid):
        a = []
        for eachLine in grid:
            a.append(eachLine[self.col])
        self.colList = a

    def rowInit(self, grid):
        self.rowList = grid[self.row]

    def getBox(self):
        a = []
        for each in self.box:
            a.append(each.getNumVal())
        return a

    def getCol(self):
        a = []
        for each in self.colList:
            a.append(each.getNumVal())
        return a

    def getRow(self):
        a = []
        for each in self.rowList:
            a.append(each.getNumVal())
        return a

    def getNumVal(self):
        return self.numval

def gridInit():
    a = []
    for line in range(0,9):
        b = []
        for col in range(0,9):
            b.append(cell(line, col, 0))
        a.append(b)
    for eachline in a:
        for each in eachline:
            each.boxInit(a)
            each.colInit(a)
            each.rowInit(a)
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
                if every.getNumVal() == 0 and num not in every.getBox() and num not in every.getCol() and num not in every.getRow():
                    poss[lineCount][colCount].append(num)
                colCount += 1
            lineCount += 1
    cell.POSS = poss

def checkPoss(grid):
    makePoss(grid)
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
        x = x[0] ### x is the row without the num
        rowToCheck = a[boxToCheck][x*3:x*3+3]
        if rowToCheck.count(0) == 1:
            grid[gridRow*3+x][boxToCheck*3+rowToCheck.index(0)].updateNumVal(num)
        elif rowToCheck.count(0) == 2:
            y = grid[gridRow*3+x][boxToCheck*3:(boxToCheck*3)+3] ### 3 instances
            a = []
            for each in y:
                if num not in each.getCol() and each.getNumVal() == 0:
                    a.append(each)
            if len(a) == 1:
                a[0].updateNumVal(num)

def basicColFind(num, gridCol, grid):
    a = [[]]
    for aBox in range(3):
        theBox = grid[aBox*3][gridCol*3].getBox()
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
            x.remove((a[each].index(num))%3)
        x = x[0] ### x is the col without the num
        colToCheck = a[boxToCheck][x::3]
        if colToCheck.count(0) == 1:
            grid[boxToCheck*3+colToCheck.index(0)][gridCol*3+x].updateNumVal(num)
        elif colToCheck.count(0) == 2:
            y = []
            for each in range(3):
                y.append(grid[boxToCheck*3+each][gridCol*3+x])
            a = []
            for each in y:
                if num not in each.getRow() and each.getNumVal() == 0:
                    a.append(each)
            if len(a) == 1:
                a[0].updateNumVal(num)

def boxPossCheck(grid):
    makePoss(grid)
    for boxRow in range(3):
        for boxCol in range(3):
            possGridBox = ''
            for each in range(3):
                    for every in range(3):
                        possGridBox += str(cell.POSS[boxRow*3+each][boxCol*3+every]).strip('[').strip(']') + ',(' + str(each*3+every) + ')'
            for eachNum in range(1,10):
                if possGridBox.count(str(eachNum)+',') == 1:
                    a = possGridBox[possGridBox.index(str(eachNum)+','):]
                    b = int(a[a.index('(')+1])
                    grid[boxRow*3+b/3][boxCol*3+b%3].updateNumVal(eachNum)
                    makePoss(grid)

#############

def loopRow(grid):
    for eachNum in range(1,10):
        for eachRow in range(3):
            basicRowFind(eachNum,eachRow,grid)

def loopCol(grid):
    for eachNum in range(1,10):
        for eachCol in range(3):
            basicColFind(eachNum,eachCol,grid)

def loopBoth(grid):
    loopRow(grid)
    loopCol(grid)

#### setup a sample puzzle ####
a = gridInit()
import examples
examples.example1(a)
makePoss(a)
printGrid(a)
print

for each in range(10):
    boxPossCheck(a)
    printGrid(a)
    print
''' 
for each in range(3):
    loopBoth(a)
    printGrid(a)
    print
'''
###############################

#### if list item == [], ignore

#### if len(column or row length) == 8, do something
