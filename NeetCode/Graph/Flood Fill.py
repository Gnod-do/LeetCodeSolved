from collections import deque

def flood_fill(image, sr, sc, new_color):
    old_color = image[sr][sc]

    if old_color == new_color:
        return image

    queue = deque([(sr, sc)])
    rows = len(image)
    cols = len(image[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    image[sr][sc] = new_color

    while queue:
        r,c = queue.popleft()

        for dr, dc in directions:
            new_r = r + dr
            new_dc = c + dc

            if 0 <= new_r < rows and 0 <= new_dc <cols and image[new_r][new_dc] == old_color:
                image[new_r][new_dc] = new_color
                queue.append((new_r,new_dc))

    return image

image1 = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print(flood_fill(image1,0,0, 2))