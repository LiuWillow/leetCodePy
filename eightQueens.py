# 下标表示行，值表示在哪一列
result = []

def isOk(row, col):
    while row >= 0:
        target = result[row - 1]
        if (target == (col - 1)) or (target == (col + 1) or (target == col)):
            return False
        row-=1
    return True

def cal8Queens(row):
    if row == 8:
        printResult(result)
        return
    for col in range(8):
        if(isOk(row, col)):
            result[row] = col
            cal8Queens(row + 1)
    
def printResult(result):
    length = len(result)
    for row in range(length):
        for col in range(length):
            rCol = result[row]
            if col == rCol:
                print("*")
            else:
                print(" ")
        print("", end=" ")

printResult(result)