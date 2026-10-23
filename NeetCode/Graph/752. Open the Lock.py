"""
Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
"""
from collections import deque

def openLock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    blocked = set(deadends)
    start = "0000"

    queue = deque([start])
    parents = {start: None}

    if start in blocked:
        return -1

    while queue:
        state = queue.popleft()
        if state == target:
            path = []

            while state is not None:
                path.append(state)
                state = parents[state]


            return len(path) - 1

        for i in range(4):
            digit = int(state[i])

            for change in (-1,1):
                new_digit = str((digit + change) % 10)

                next_state = (state[:i] + new_digit + state[i + 1:])

                if next_state not in blocked and next_state not in parents:
                    parents[next_state] = state
                    queue.append(next_state)
    return -1

print(openLock(["8888"],"0009"))




