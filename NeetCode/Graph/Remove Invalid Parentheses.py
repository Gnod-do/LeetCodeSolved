def isValid(s):
    count = 0

    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

            if count < 0:
                return False

    return count == 0


def validParentheses(s):
    q = [s]
    visited = set()
    visited.add(s)
    found = False
    res = []
    while q:
        curr = q.pop(0)

        if isValid(curr):
            res.append(curr)
            found = True

        if found:
            continue

        for c in range(len(curr)):
            if curr[c] != '(' and curr[c] != ')':
                continue

            next_s = curr[:c] + curr[c+1:]

            if next_s not in visited:
                visited.add(next_s)
                q.append(next_s)

    return res


s = '(a)())()'
print(validParentheses(s))