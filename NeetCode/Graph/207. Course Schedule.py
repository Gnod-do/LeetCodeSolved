def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    visited = [False] * numCourses
    recStack = [False] * numCourses

    adj = [[] for _ in range(numCourses)]
    for pos, pre in prerequisites:
        adj[pre].append(pos)


    def dfs(u):
        if recStack[u]:
            return True

        if visited[u]:
            return False

        visited[u] = True
        recStack[u] = True
        for neighbor in adj[u]:
            if dfs(neighbor):
                return True

        recStack[u] = False
        return False

    for i in range(numCourses):
        if not visited[i] and dfs(i):
            return False

    return True

numCourses = 2
prerequisites = [[1,0], [0,1]]
print(canFinish(numCourses, prerequisites))
