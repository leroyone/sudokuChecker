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

    #### not needed?
    ''' 
    def getRawBox(self):
        return self.box
    '''

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


def boxPossCheck(grid):
    makePoss(grid) #replace with cell.POSS
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
                    makePoss(grid) #replace with ...something??

##############################################################################################################################################

def updatePoss(num, target, without):
    ''' 
    num: number to be removed from other cells
    target: string, letter(r,c,b) and number(0-9) pertaining to which to update
    without: list telling which rows or columns to ignore
    Removes the number from all adjacent Cells and Box if True
    '''
    try:
        x = int(target[1])
    except:
        print 'Probably incorrect input here'
        return
    #rows
    if target[0] == 'r':
        for eachCell in range(9):
            if eachCell not in without and num in cell.POSS[x][eachCell]:
                cell.POSS[x][eachCell].remove(num)
    #cols
    elif target[0] == 'c':
        for eachCell in range(9):
            if eachCell not in without and num in cell.POSS[eachCell][x]:
                cell.POSS[eachCell][x].remove(num)
    #boxes
    elif target[0] == 'b':
        boxRow = range(x/3*3,x/3*3+3)
        boxCol = range(x%3*3,x%3*3+3)
        print boxRow
        print boxCol
        count = 0
        for eachRow in boxRow:
            for eachCol in boxCol:
                if num in cell.POSS[eachRow][eachCol] and count not in without:
                    cell.POSS[eachRow][eachCol].remove(num)
                count += 1


def numInRowOne():
    for possRow in cell.POSS:
        pass









##############################################################################################################################################

#### setup a sample puzzle ####
a = gridInit()
import examples
examples.example3(a)
makePoss(a)
printGrid(a)
print

''' 
while True:
    checker = cell.POSS[:]
    loopTwo(a)
    loopOne(a)
    if cell.POSS == checker:
        printGrid(a)
        break

print
checkPossSpecial(a)
'''
for each in cell.POSS:
    print each
print

updatePoss(5,'b1',[1])

for each in cell.POSS:
    print each
print

###############################

#### if len(column or row length) == 8, do something
