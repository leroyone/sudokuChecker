#!/usr/bin/python

a = []

for line in range(1,10):
    b = []
    for column in range(1,10):
        b.append(0)
    a.append(b)

###### maker #####

a[0][6] = 5
a[0][7] = 2
a[1][3] = 5
a[1][4] = 3
a[2][1] = 3
a[2][3] = 4
a[2][4] = 7
a[3][0] = 1
a[3][1] = 4
a[3][6] = 2
a[4][2] = 7
a[4][3] = 1
a[4][5] = 5
a[4][6] = 6
a[5][2] = 2
a[5][7] = 7
a[5][8] = 5
a[6][4] = 4
a[6][5] = 3
a[6][7] = 8
a[7][4] = 6
a[7][5] = 7
a[8][1] = 6
a[8][2] = 8

##############

for each in a:
    print each


#### check if number not in column or row
def initcheck(grid):
    pass


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
