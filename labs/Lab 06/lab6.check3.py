import lab06_util
file = input("Enter a filename: ")
bd = lab06_util.read_sudoku(file)

def verify_board(bd):  
    for i in range(9):
        for j in range(9):
            if bd[i][j] == ".":
                return False
            if ok_to_add(bd, i, j, bd[i][j]) == False:
                return False
    return True

def ok_to_add(bd, row, col, num):
    if row > 8 or col > 8:
        return False
    og = bd[row][col]
    bd[row][col] = "."
    for i in range(9):
        if bd[row][i] == num:
            bd[row][col] = og
            return False
    for j in range(9):
        if bd[j][col] == num:
            bd[row][col] = og
            return False
    startrow = (row // 3) * 3  
    startcol = (col // 3) * 3   
    for i in range(startrow, startrow + 3):
        for j in range(startcol, startcol + 3):
            if bd[i][j] == num:
                bd[row][col] = og
                return False
    bd[row][col] = num          
    return True

while verify_board(bd) != True:
    row = int(input("Enter a row (starting at index 0): "))
    column = int(input("Enter a column (starting at index 0): "))
    num = input("Enter a number: ")   
    if ok_to_add(bd, row, column, num) != True:
        print("False")
    for i in range(9):
        print()
        if i == 0:
            print("-" * 25) 
        if i == 3:
            print("-" * 25)
        if i == 6:
            print("-" * 25)       
        for j in range(9):
            if j == 0:
                print("|", end= ' ')        
            if j == 3:
                print("|", end= ' ')
            if j == 6:
                print("|", end= ' ') 
            print(bd[i][j], end= " ")
        print("|", end= ' ')    
    print()
    print("-" * 25)
    
while verify_board(bd) == True:
    row = int(input("Enter a row (starting at index 0): "))
    column = int(input("Enter a column (starting at index 0): "))
    num = input("Enter a number: ")       
    if ok_to_add(bd, row, column, num) == True:
            print("True")
    for i in range(9):
        print()
        if i == 0:
            print("-" * 25) 
        if i == 3:
            print("-" * 25)
        if i == 6:
            print("-" * 25)       
        for j in range(9):
            if j == 0:
                print("|", end= ' ')        
            if j == 3:
                print("|", end= ' ')
            if j == 6:
                print("|", end= ' ') 
            print(bd[i][j], end= " ")
        print("|", end= ' ')    
    print()
    print("-" * 25)
    break


        