class Solution(object):
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        k = 0

        for i in range(n - 1):
            if matrix[i][0] == target or matrix[i + 1][0] == target:
                return True
            elif matrix[i][0] < target < matrix[i + 1][0]:
                k = i
                break
            if i + 1 == len(matrix) - 1:
                k = i + 1

        for i in range(m):
            if matrix[k][i] == target:
                return True

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 30
sol = Solution()
print(sol.searchMatrix(matrix, target))