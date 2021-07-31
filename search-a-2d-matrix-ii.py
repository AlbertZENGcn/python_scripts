class Solution:
    def findNumberIn2DArray(self, matrix, target):
        i= 0
        j= len(matrix)-1
        while j>=0 and i<len(matrix[0]):
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                print("True")
        print("False")

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
s = Solution()
s.findNumberIn2DArray(matrix, target)
