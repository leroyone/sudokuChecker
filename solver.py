#!/usr/bin/python -B

class cell():
    POSS = None
    THECACHE = []

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
        count = 0
        for eachRow in boxRow:
            for eachCol in boxCol:
                if num in cell.POSS[eachRow][eachCol] and count not in without:
                    cell.POSS[eachRow][eachCol].remove(num)
                count += 1

##############################################################################################################################################

def rowStr(row):
    ''' 
    row: int representing row
    returns that row as a string with number delimiters
    '''
    ans = ''
    cellNum = 0
    for eachCell in cell.POSS[row]:
        ans += str(eachCell).strip(']') + ', ]' + str(cellNum)
        cellNum += 1
    return ans

def colStr(col):
    ''' 
    col: int representing col
    returns that col as a string with number delimiters
    '''
    ans = ''
    cellNum = 0
    for eachRow in cell.POSS:
        ans += str(eachRow[col]).strip(']') + ', ]' + str(cellNum)
        cellNum += 1
    return ans

def boxStr(box):
    ''' 
    box: int representing box
    returns that box as a string with number delimeters
    '''
    ans = ''
    cellNum = 0
    for eachRow in range(3):
        for eachCol in range(3):
            ans += str(cell.POSS[eachRow+(box/3*3)][eachCol+(box%3*3)]).strip(']') + ', ]' + str(cellNum)
            cellNum += 1
    return ans

def cacheIt(subject, locality, toCache):
    ''' 
    subject: str, name of function
    index: int
    toCache: str, particular cell
    '''
    cell.THECACHE.append(subject + str(locality) + str(toCache))


def cacheCheck(subject, locality, toCheck):
    ''' 
    subject: str, name of function
    index: int
    toCache: str, particular cell
    '''
    a = subject + str(locality) + str(toCheck)
    return a not in cell.THECACHE

def colList(col):
    ''' 
    returns a list of cells in a column
    '''
    ans = []
    for eachRow in cell.POSS:
        ans.append(eachRow[col])
    return ans

def rowColtoBox(row, col):
    ''' 
    returns box number from cell row and col
    '''
    return row/3*3+col/3

def boxCellToRow(box, boxCell):
    ''' 
    returns cell row from box cell
    '''
    return box/3*3+boxCell/3

def boxCellToCol(box, boxCell):
    ''' 
    returns cell col from boxx cell
    '''
    return box%3*3+boxCell%3

def boxList(box):
    ''' 
    returns a list of cells inn a box
    '''
    ans = []
    for eachRow in cell.POSS[box/3*3:box/3*3+3]:
        ans += eachRow[box%3*3:box%3*3+3]
    return ans

##############################################################################################################################################

def numInRowOne(num, grid):
    ''' 
    num: int
    If number occurs once only in row: grid, cell, col and box updated
    '''
    numCheck = str(num)+','
    for possRow in range(9):
        check = rowStr(possRow)
        if check.count(numCheck) == 1:
            col = int(check[check.index(']',check.index(numCheck))+1])
            cell.POSS[possRow][col] = []
            grid[possRow][col].updateNumVal(num)
            updatePoss(num, 'c'+str(col), [possRow])
            updatePoss(num, 'b'+str((possRow/3*3)+col/3), [(possRow%3*3)+((col%3*3)/3)])

def numInColOne(num, grid):
    ''' 
    num: int
    If number occurs once only in col: grid, cell, row and box updated
    '''
    numCheck = str(num)+','
    for possCol in range(9):
        check = colStr(possCol)
        if check.count(numCheck) == 1:
            row = int(check[check.index(']',check.index(numCheck))+1])
            cell.POSS[row][possCol] = []
            grid[row][possCol].updateNumVal(num)
            updatePoss(num, 'r'+str(row), [possCol])
            updatePoss(num, 'b'+str((row/3*3)+possCol/3), [(row%3*3)+((possCol%3*3)/3)])

def numInBoxOne(num, grid):
    ''' 
    num: int
    If number occurs one only in box: grid, cell, row and col updated
    '''
    numCheck = str(num)+','
    for box in range(9):
        check = boxStr(box)
        if check.count(numCheck) == 1:
            boxCell = int(check[check.index(']',check.index(numCheck))+1])
            row = box/3*3 + boxCell/3
            col = box%3*3 + boxCell%3
            cell.POSS[row][col] = []
            grid[row][col].updateNumVal(num)
            updatePoss(num, 'r'+str(row), [col])
            updatePoss(num, 'c'+str(col), [row])

def numInRowTwoThreeFour(num, grid): ### To Do!!
    ''' 
    '''
    pass

##############################################################################################################################################

def lenCellOne(grid):
    ''' 
    if any cell length is 1: grid, cell, row, col and box updated
    '''
    for row in range(9):
        for col in range(9):
            if len(cell.POSS[row][col]) == 1:
                num = cell.POSS[row][col][0]
                grid[row][col].updateNumVal(num)
                updatePoss(num, 'r'+str(row), [col])
                updatePoss(num, 'c'+str(col), [row])
                updatePoss(num, 'b'+str((row/3*3)+col/3), [(row%3*3)+((col%3*3)/3)])
                cell.POSS[row][col] = []

def lenRowTwo():
    ''' 
    if two identical cells in row have len2: update row
    '''
    for row in range(9):
        for col in cell.POSS[row]:
            if len(col) == 2:
                a = col # the pair cell
                if cell.POSS[row].count(a) == 2 and cacheCheck('lenRowTwo', row, a):
                    x = cell.POSS[row].index(a) # index of first pair
                    without = [x, cell.POSS[row].index(a,x+1)]
                    cacheIt('lenRowTwo', row, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'r'+str(row), without)

def lenColTwo():
    ''' 
    if two identical cells in col have len2: update col
    '''
    for eachCol in range(9):
        col = colList(eachCol)
        for row in col:
            if len(row) == 2:
                a = row #the pair cell
                if col.count(a) == 2 and cacheCheck('lenColTwo', eachCol, a):
                    x = col.index(a) #index of first pair
                    without = [x, col.index(a,x+1)]
                    cacheIt('lenColTwo', eachCol, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'c'+str(eachCol), without)

def lenBoxTwo():
    ''' 
    if two identical cells in box have len2: update box
    '''
    for boxNum in range(9):
        box = boxList(boxNum)
        for eachCell in box:
            if len(eachCell) == 2:
                a = eachCell #the pair cell
                if box.count(a) == 2 and cacheCheck('lenBoxTwo', boxNum, a):
                    x = box.index(a) #index of first pair
                    without = [x, box.index(a, x+1)]
                    cacheIt('lenBoxTwo', boxNum, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'b'+str(boxNum), without)

def lenRowThree():
    ''' 
    if two identical cells in row have len2: update row
    '''
    for row in range(9):
        for col in cell.POSS[row]:
            if len(col) == 3:
                a = col # the triple cell
                if cell.POSS[row].count(a) == 3 and cacheCheck('lenRowThree', row, a):
                    x = cell.POSS[row].index(a) # index of first triple
                    y = cell.POSS[row].index(a, x+1)
                    without = [x, y, cell.POSS[row].index(a,y+1)]
                    cacheIt('lenRowThree', row, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'r'+str(row), without)

def lenColThree():
    ''' 
    if three identical cells in col have len3: update col
    '''
    for eachCol in range(9):
        col = colList(eachCol)
        for row in col:
            if len(row) == 3:
                a = row #the triple cell
                if col.count(a) == 3 and cacheCheck('lenColThree', eachCol, a):
                    x = col.index(a) #index of first triple
                    y = col.index(a, x+1)
                    without = [x, y, col.index(a, y+1)]
                    cacheIt('lenColThree', eachCol, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'c'+str(eachCol), without)

def lenBoxThree():
    ''' 
    if three identical cells in box have len3: update box
    '''
    for boxNum in range(9):
        box = boxList(boxNum)
        for eachCell in box:
            if len(eachCell) == 3:
                a = eachCell #the triple cell
                if box.count(a) == 3 and cacheCheck('lenBoxThree', boxNum, a):
                    x = box.index(a) #index of first triple
                    y = box.index(a, x+1)
                    without = [x, y, box.index(a, y+1)]
                    cacheIt('lenBoxThree', boxNum, a)
                    for eachNum in a:
                        updatePoss(eachNum, 'b'+str(boxNum), without)

##############################################################################################################################################

def lenRowTwoThree():
    ''' 
    if not lenRowTwo()
    if len2 cel numbers in two identical len3 cells: remove 3rd from row
    if len3 cells in same box: remove 3rd from box
    '''
    for row in range(9):
        for col in cell.POSS[row]:
            if len(col) == 2 and cacheCheck('lenRowTwo', row, col):
                a = col #the pair cell
                for nextCol in cell.POSS[row]:
                    if len(nextCol) == 3 and a[0] in nextCol and a[1] in nextCol:
                        b = nextCol #the triple cell
                        if cell.POSS[row].count(b) == 2 and cacheCheck('lenRowTwoThree', row, b):
                            x = cell.POSS[row].index(b)
                            y = cell.POSS[row].index(b, x+1)
                            cacheIt('lenRowTwoThree', row, b)
                            for eachTest in b:
                                if eachTest not in a:
                                    c = eachTest #the remaining number
                            updatePoss(c, 'r'+str(row), [x,y])
                            z = cell.POSS[row].index(a)
                            for eachNum in a:
                                updatePoss(eachNum, 'r'+str(row), [x,y,z])
                            if x/3 == y/3:
                                updatePoss(c, 'b'+str(rowColtoBox(row, x)), [(row/3*3+x%3),(row/3*3+y%3)])


def lenColTwoThree(grid): ### To Do!!
    ''' 
    if not lenColTwo()
    if len2 cel numbers in two identical len3 cells: remove 3rd from col
    if len3 cells in same box: remove 3rd from box
    '''
    pass

def lenBoxTwoThree(grid): ### To Do!!
    ''' 
    if not lenBoxTwo()
    if len2 cel numbers in two identical len3 cells: remove 3rd from box
    if len3 cells in same row or col: remove 3rd from row or col
    '''
    pass

##############################################################################################################################################

def numInRowInBox(): ### To do!!
    ''' 
    if number in row is only in box, remove from box
    '''
    for row in range(9):
        for each in cell.POSS[row]:
            pass

def numInRowInBox(): ### To do!!
    ''' 
    if number in col is only in box, remove from box
    '''
    pass

def numInBoxInLine(): ### To do!!
    ''' 
    if number in box is only in line, remove from line
    '''
    pass

##############################################################################################################################################

def looper():
    for every in range(1,10):
        numInRowOne(every, exampleGrid)
        numInColOne(every, exampleGrid)
        numInBoxOne(every, exampleGrid)
    lenCellOne(exampleGrid)
    lenRowTwo()
    lenColTwo()
    lenBoxTwo()
    lenRowThree()
    lenColThree()
    lenBoxThree()
    lenRowTwoThree()
    ''' 
    print
    for each in cell.POSS:
        print each
    print
    '''
    printGrid(exampleGrid)
    print

#### setup a sample puzzle ####
exampleGrid = gridInit()
import examples
examples.example3(exampleGrid)
makePoss(exampleGrid)
printGrid(exampleGrid)
print
###############################

import copy

count = 0
while True:
    checker = copy.deepcopy(cell.POSS)
    looper()
    if cell.POSS == checker:
        print str(count) + ' loops'
        break
    count += 1

print
for each in cell.POSS:
    print each

print
print cell.THECACHE
