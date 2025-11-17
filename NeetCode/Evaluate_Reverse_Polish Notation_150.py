class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif char == '-':
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b-a)
            elif char == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif char == '/':
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(char)

        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens))