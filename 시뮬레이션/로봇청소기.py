from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0,1,0,-1]
queue = deque()
queue.append((r,c,d))
count = 0
while queue:
    x, y, direction = queue.popleft()
    if room[x][y] == 0: #1번
        room[x][y] = 2
        count += 1
    room_cleand = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<= nx < N and 0<= ny < M and room[nx][ny] == 0:
            room_cleand = False
    if room_cleand == True:
        backward = (direction+2)%4
        nx, ny = x+dx[backward], y+dy[backward]
        if 0<= nx < N and 0<= ny < M and room[nx][ny] != 1:
            queue.append((nx, ny, direction))
        else:
            break
    elif room_cleand == False:
        direction = (direction+3)%4
        nx, ny = x+dx[direction], y+dy[direction]
        if 0<= nx < N and 0<= ny < M and room[nx][ny] == 0:
            queue.append((nx,ny,direction))
        else:
            queue.append((x,y,direction))
print(count)
