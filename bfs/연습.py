from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque()

    for word in words:  # 후보 단어 삽입
        diff = 0
        for idx in range(len(word)):
            if begin[idx] != word[idx]:
                diff += 1
        if diff == 1:
            queue.append((word, 1))
            visited[words.index(word)] = True

    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            return cnt
        for word in words:
            if not visited[words.index(word)]:
                diff = 0
                for idx in range(len(word)):
                    if cur[idx] != word[idx]:
                        diff += 1
                if diff == 1:
                    queue.append((word, cnt + 1))
                    visited[words.index(word)] = True
    return 0
