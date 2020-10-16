





class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix) == 0:
            return False
        
        row = 0
        col = len(matrix[0])-1
        # print(len(matrix))
        
        while (row < len(matrix) and col >= 0):
            print(row,'  ', col)
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row = row + 1
            elif target < matrix[row][col]:
                col = col - 1
                
        return False