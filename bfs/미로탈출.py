from collections import deque
def finding(maps, start, end):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    distance = [[0 for i in range(m)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    directions = [(-1,0), (1,0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != 'X': 
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if (nx, ny) == end:
                        return distance[nx][ny]
                    queue.append((nx,ny))
    return -1
        
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    for y in range(n):
        for x in range(m):
            if maps[y][x] == "S":
                start = (y,x)
            elif maps[y][x] == "L":
                lever = (y,x)
            elif maps[y][x] == "E":
                exit = (y,x)
    start_to_lever = finding(maps, start, lever)
    lever_to_exit= finding(maps, lever, exit)
    if start_to_lever == -1 or lever_to_exit == -1:
        return -1
    return start_to_lever + lever_to_exit

print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))