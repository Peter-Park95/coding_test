from collections import deque
N, K = map(int,input().split())
def moving(start, target):
    visited = [False] * 100001
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        pos, time = queue.popleft()
        if pos == target:
            return time
        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos < 100001 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time+1))
print(moving(N,K))