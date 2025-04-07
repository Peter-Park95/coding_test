from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append((0,0))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 
                queue.append((nx,ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))