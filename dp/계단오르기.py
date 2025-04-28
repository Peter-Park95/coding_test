S = int(input())
step = [0] + list(int(input()) for _ in range(S))
score = [0] * (S+1)
if S == 1:
    print(step[S])
else:
    score[1] = step[1]
    score[2] = step[1] + step[2]
    for i in range(3, S+1):
        score[i] = max(score[i-3]+ step[i-1]+step[i], score[i-2]+ step[i])
    print(score[S])
