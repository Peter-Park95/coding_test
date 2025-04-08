import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def bfs(maps,n,m):
    queue = deque()
    queue.append((0,0))
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    return maps[n-1][m-1] 

print(bfs(map,n,m))