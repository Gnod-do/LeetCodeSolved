class Solution(object):
    def isValid(self, s):
        stack = []
        closingParentheses = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in closingParentheses:
                if stack and closingParentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False







s = "()[]{})"
sol = Solution()
print(sol.isValid(s))