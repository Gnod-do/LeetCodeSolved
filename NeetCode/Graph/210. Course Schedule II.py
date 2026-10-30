class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """


sol = Solution()

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses, prerequisites))