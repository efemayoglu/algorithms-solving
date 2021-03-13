class SubrectangleQueries:

    a = [[]]

    def __init__(self, rectangle: [[int]]):
        self.a = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        for i in range(row1, row2+1): #4
            if i <= row2+1: 
                for j in range(col1, col2+1):
                    if j<= col2+1:
                        self.a[i][j] = newValue
        return None

    def getValue(self, row: int, col: int) -> int:
        return self.a[row][col]            
        

s = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
 

s.updateSubrectangle(0, 0, 3, 2, 5)
print(s.a)
s.updateSubrectangle(3, 0, 3, 2, 10)
print(s.a)
print(s.getValue(3, 1))
print(s.getValue(0, 2))
# The initial rectangle (4x3) looks like:
# 1 2 1
# 4 3 4
# 3 2 1
# 1 1 1
# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)