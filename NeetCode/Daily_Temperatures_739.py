class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = [] # [tmp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                tmp, index = stack.pop()
                res[index] = i - index
            stack.append([t,i])
        return res

temperatures = [30,60,90]
sol = Solution()
print(sol.dailyTemperatures(temperatures))