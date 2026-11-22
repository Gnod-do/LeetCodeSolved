from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        words = set(wordList)

        if endWord not in words:
            return 0

        visited = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    if word[i] == c:
                        continue

                    new_word = word[:i] + c + word[i + 1:]

                    if new_word not in visited and new_word in words:
                        queue.append((new_word, length + 1))
                        visited.add(new_word)

        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
print(sol.ladderLength(beginWord,endWord,wordList))