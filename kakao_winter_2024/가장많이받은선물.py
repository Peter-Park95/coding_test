def solution(friends, gifts):
    max_take = 0
    give_take_graph = [[0]*len(friends) for _ in range(len(friends))]
    gift_score = [0] * len(friends)
    for gift in gifts: # 준사람 받은사람 그래프 작성
        p = gift.split()
        give_take_graph[friends.index(p[0])][friends.index(p[1])] += 1
    for idx, friend in enumerate(friends): #선물지수 작성
        give_count = 0
        take_count = 0
        for gift in gifts:
            g = gift.split()
            if g[0] == friend:
                give_count += 1
            if g[1] == friend:
                take_count += 1
        gift_score[idx] = give_count - take_count
    for idx, friend in enumerate(friends):
        count = 0
        for j in range(0, len(friends)):
            if give_take_graph[idx][j] > give_take_graph[j][idx]:
                count += 1
            if give_take_graph[idx][j] == give_take_graph[j][idx] and gift_score[idx] > gift_score[j]:
                count += 1
        max_take = max(max_take, count)
    return max_take


