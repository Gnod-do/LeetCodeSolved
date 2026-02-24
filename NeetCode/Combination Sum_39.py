class Solution:
    def combinationSum(self, candidates, target):
        curCom = []
        res = []

        self.makeCombinations(candidates, target, curCom, res, 0)
        return res

    def makeCombinations(self, arr, remSum, curCom, res, index):
        if remSum == 0:
            res.append(list(curCom))
            return

        if remSum < 0 or index >= len(arr):
            return

        curCom.append(arr[index])
        self.makeCombinations(arr, remSum - arr[index], curCom, res, index)

        curCom.pop()
        self.makeCombinations(arr, remSum, curCom, res, index + 1)

candidates = [2,3,5]
target = 8
sol = Solution()
print(sol.combinationSum(candidates, target))