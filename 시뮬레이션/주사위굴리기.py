from collections import deque
N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int,input().split()))

dice = {'up' : 0, 'down': 0, 'west': 0, 'east': 0, 'north': 0, 'south': 0}
queue = deque()
queue.append((x,y))
dice['down'] = maps[x][y]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for o in order:
    x, y = queue.popleft()
    nx, ny = x+dx[o-1], y+dy[o-1]
    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
        if o == 1: #동쪽으로 이동
            temp = dice['down']
            dice['down'] = dice['east']
            dice['east'] = dice['up']
            dice['up'] = dice['west']
            dice['west'] = temp
        elif o == 2: #서쪽으로 이동
            temp = dice['down']
            dice['down'] = dice['west']
            dice['west'] = dice['up']
            dice['up'] = dice['east']
            dice['east'] = temp
        elif o == 3: #북쪽으로 이동
            temp = dice['down']
            dice['down'] = dice['north']
            dice['north'] = dice['up']
            dice['up'] = dice['south']
            dice['south'] = temp
        elif o == 4: #남남쪽으로 이동
            temp = dice['down']
            dice['down'] = dice['south']
            dice['south'] = dice['up']
            dice['up'] = dice['north']
            dice['north'] = temp
        if maps[nx][ny] == 0:
            maps[nx][ny] = dice['down']
        else:
            dice['down'] = maps[nx][ny]
            maps[nx][ny] = 0
        print(dice['up'])
        queue.append((nx,ny))
    else:
        queue.append((x,y))


