import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
def bfs_tomato(M,N, maps):
    day = 0
    queue = deque()
    for i in range(N): #시작점 찾기(익은 토마토 모두 찾기)
        for j in range(M):
            if maps[i][j] == 1:
                queue.append((i,j))
    directions = [(1,0), (-1,0), (0,-1), (0,1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    day = 0
    for row in maps:
        if 0 in row:
            return -1
        day = max(day, max(row))
    return day - 1
print(bfs_tomato(M,N,maps))
        


