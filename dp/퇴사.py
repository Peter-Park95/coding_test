N = int(input())
consulting = []
income = [0] * N
for _ in range(N):
    t, p = map(int, input().split())
    consulting.append((t,p))

for day in (0, N+1):
    income[day] = income[day-1] + consulting[day][1]
    