from itertools import combinations
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house_location = []
chicken_location =[]
total_chicken_distance = 99999999
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house_location.append((i,j))
        if city[i][j] == 2:
            chicken_location.append((i,j))

for c in combinations(chicken_location, M):
    city_chicken_distance = []
    for house in house_location:
        distance = []
        for idx in range(M):
            distance.append(abs(house[0]-c[idx][0])+abs(house[1]-c[idx][1]))
        city_chicken_distance.append(min(distance))
    total_chicken_distance = min(total_chicken_distance,sum(city_chicken_distance))
print(total_chicken_distance)