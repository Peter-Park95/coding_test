# from collections import deque


# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# count = 0
# room = []
# for i in range(N):
#     room.append(list(map(int, input().split())))
# directions = [[-1,0], [0,1], [1,0], [0,-1]]
# queue = deque()
# queue.append([[r,c],d, count])
# dx = [-1, 0, 1, 0]
# dy = [0,1,0,-1]
# while queue:
#     [x, y], direct, cnt = queue.popleft()
#     if room[x][y] == 0: # 1번
#         room[x][y] = 1
#         cnt += 1
#     if (not room[x+1][y] or room[x+1][y] == 1) and (not room[x-1][y] or room[x-1][y]) and (not room[x][y+1] or room[x][y+1]) and (not room[x][y-1] or room[x][y-1]): #2번
#         if directions[direct] == [-1,0]:
#             if room[x+1][y]:
#                 queue.append([x+1,y], direct, cnt)
#                 continue
#         if directions[direct] == [0,1]:
#             if room[x][y-1]:
#                 queue.append([x,y-1], direct, cnt)
#                 continue
#         if directions[direct] == [1,0]:
#             if room[x-1][y]:
#                 queue.append([x-1,y], direct, cnt)
#                 continue
#         if directions[direct] == [0,-1]:
#             if room[x][y+1]:
#                 queue.append([x,y+1], direct, cnt)
#                 continue
#         print(cnt)
#     else:
#         direct -= 1
#         if directions[direct] == [-1,0]:

lst = []
lst.append(1,2,3,4)