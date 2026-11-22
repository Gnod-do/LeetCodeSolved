def line_reflection(points):
    minX = min(p[0] for p in points)
    maxX = max(p[0] for p in points)
    s = minX + maxX

    setP = set()
    for p in points:
        setP.add(tuple(p))

    for point in points:
        x_new = s - point[0]
        ref_point = (x_new, point[1])
        if ref_point not in setP:
            return False

    return True




points = [[10,1],[1,1],[10,2],[1,2],[5,9],[6,9]]
print(line_reflection(points))