from itertools import combinations
N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
total_ability_score = 0
min_score_gap = float('inf')
for idx in range(N):
    total_ability_score += sum(ability[idx])
player = [i for i in range(1, N+1)]
for team1 in combinations(player, N//2):
    team2 = list()
    for i in range(1, N+1):
        if i not in(team1):
            team2.append(i)
    team1_score = 0
    team2_score = 0
    for idx1 in range(len(team1)):
        for idx2 in range(idx1+1,len(team1)):
            team1_score += (ability[team1[idx1]-1][team1[idx2]-1] + ability[team1[idx2]-1][team1[idx1]-1])
            team2_score += (ability[team2[idx1]-1][team2[idx2]-1] + ability[team2[idx2]-1][team2[idx1]-1])
    
    min_score_gap = min(min_score_gap, abs(team1_score-team2_score))
print(min_score_gap)