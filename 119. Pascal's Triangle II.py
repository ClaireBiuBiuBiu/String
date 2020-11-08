'''
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        r=[1,1]
        for i in range(rowIndex-1):
            temp=[1]
            for i in range(len(r)-1):
                temp.append(r[i]+r[i+1])
            temp.append(1)
            r = temp.copy()
        return r