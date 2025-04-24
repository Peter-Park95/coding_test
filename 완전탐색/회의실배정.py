from collections import deque
N = int(input())
meetings = deque()
count = 0
current_time = 0
for i in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings = deque(sorted(meetings, key=lambda time: (time[1], time[0])))
while meetings:
    start_time, end_time = meetings.popleft()
    if start_time >= current_time:
        count += 1
        current_time = end_time
