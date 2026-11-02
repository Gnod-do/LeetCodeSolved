'''
1. Xây exist[]
2. Xây graph -> duyệt hết check 2 word kề trong words, so sánh chữ cái bắt đầu. Sau đó đẩy vào graph, đồng thời tăng indegree.
3. Dùng Kahn's BFS để duyệt và trả về kết quả.
Note: Dùng ord() và chr() để chuyển đổi giữa số ở bảng mã ASCII và chữ cái.
'''
from collections import deque

def alienDic(words):
    graph = [[] for _ in range(26)]
    exist = [False] * 26
    indegree = [0] * 26

    # Build exist
    for word in words:
        for u in word:
            exist[ord(u) - ord('a')] = True

    # Build graph
    for i in range(len(words) - 1):
        pre, pos = words[i], words[i + 1]
        j = 0
        minLen = min(len(pre), len(pos))

        while j < minLen and pre[j] == pos[j]:
            j += 1

        if j < minLen:
            u = ord(pre[j]) - ord('a')
            v = ord(pos[j]) - ord('a')
            graph[u].append(v)
            indegree[v] += 1
        elif len(pre) > len(pos):
            return ""

    queue = deque(i for i in range(26) if exist[i] and indegree[i] == 0)
    res = []

    while queue:
        u = queue.popleft()
        res.append(chr(u + ord('a')))
        for v in graph[u]:
            indegree[v] -= 1

            if indegree[v] == 0:
                queue.append(v)

    if len(res) != sum(exist):
        return ""
    return ''.join(res)



words = ["baa", "abcd", "abca", "cab", "cad"]
print(alienDic(words))