class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w = 0
        count = 1

        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i] == chars[i+1]:
                count += 1
            else:
                chars[w] = chars[i]
                w += 1

                if count > 1:
                    for d in str(count):
                        chars[w] = d
                        w += 1
                count = 1

        return w

chars = ["a", "a", "b", "b", "c", "c", "c"]
sol = Solution()
print(sol.compress(chars))