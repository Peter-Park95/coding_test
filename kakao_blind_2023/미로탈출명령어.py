from collections import deque

def solution(n, m, x, y, r, c, k):
    directions_ch = ['d', 'l', 'r', 'u']
    directions = [(1,0), (0,-1), (0, 1), (-1, 0)]
    found = False
    def is_possible(cur_x, cur_y, count):
        distance = abs(r-cur_x) + abs(c-cur_y)
        return (k-count) >= distance  and (k - count - distance) % 2 == 0

    queue = deque()
    queue.append((x,y,0,''))
    while queue:
        x, y, cnt, letter = queue.popleft()
        if not is_possible(x,y,cnt) or cnt > k:
            continue
        if (x,y) == (r,c) and cnt == k:
            return letter
        for ch, (dx, dy) in zip(directions_ch, directions):
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                queue.append((nx, ny, cnt+1, letter+ch))
    return 'impossible'
print(solution(3,4,2,3,3,1,5))
