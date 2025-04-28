from collections import deque
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
size, time = 2, 0
ate, x, y = 0,0,0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
for i in range(N): #시작점 찾기
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

def bfs(start_x, start_y, size):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0
    fish = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if space[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    if 0 < space[nx][ny] < size:
                        fish.append((visited[nx][ny], nx, ny))
    return sorted(fish)

while True:
    fishes = bfs(x,y,size)
    if not fishes:
        break
    distance, nx, ny = fishes[0]
    time += distance
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    space[nx][ny] = 0
    x, y = nx, ny
print(time)
