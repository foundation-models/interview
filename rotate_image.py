
def swap(matrix, n, i, j):
    tmp = matrix[i][j]
    matrix[i][j] = matrix[n-j][i]
    matrix[n-j][i] =  matrix[n-i][n-j]
    matrix[n-i][n-j] = matrix[j][n-i]
    matrix[j][n-i] = tmp
            
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

            
        n = len(matrix[0]) - 1
        for i in range((n+1)//2):
            for j in range(0, n-i):
                swap(matrix, n, i, j)
            
        return matrix
