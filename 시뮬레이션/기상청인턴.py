N, K = map(int, input().split())
temperature = list(map(int, input().split()))
temp_sum = []
for i in range(0, N-K+1):
    total = 0
    for j in range(i, i+K):
        total += temperature[j]
    temp_sum.append(total)
print(max(temp_sum))