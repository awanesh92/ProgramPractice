from typing import List
class SubrectangleQueries:
    
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1 , row2, col2, newValue):
        '''for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rectangle[i][j]=newValue '''
        val=[newValue]*(col2-col1+1)
        for i in range(row1,row2+1):
            self.rectangle[i][col1:col2+1]=val

    def getValue(self, row, col):
        return self.rectangle[row][col]

q=SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])

q.updateSubrectangle(0,0,3,2,5)
assert q.rectangle == [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]
assert q.getValue(3, 1) == 5
q.updateSubrectangle(3,0,3,2,10)
assert q.rectangle == [[5, 5, 5], [5, 5, 5], [5, 5, 5], [10, 10, 10]]
assert q.getValue(3, 1) == 10
assert q.getValue(3, 1) == 10