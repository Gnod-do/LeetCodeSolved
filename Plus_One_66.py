class Solution:
    def plusOne(self, digits):
        digits.reverse()
        carry, i = 1, 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    carry = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        digits.reverse()

        return digits

digits = [9,9,9]
solution = Solution()
print(solution.plusOne(digits))