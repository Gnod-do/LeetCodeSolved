from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        res = []

        for pos, pre in prerequisites:
            adj[pre].append(pos)
            indegree[pos] += 1

        for u in range(numCourses):
            if indegree[u] == 0:
                queue.append(u)

        while queue:
            top = queue.popleft()
            res.append(top)

            for u in adj[top]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.append(u)

        return res if len(res) == numCourses else []

sol = Solution()

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses, prerequisites))