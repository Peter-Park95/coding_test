from collections import deque
def is_one_letter_diff(a, b):
    diff = 0
    for ch1, ch2 in zip(a, b):
        if ch1 != ch2:
            diff += 1
    return True if diff == 1 else False

def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque()
    for idx, word in enumerate(words): #후보단어 큐에 삽입
        if is_one_letter_diff(begin, word):
            queue.append((word, 1))
            visited[idx] = True
    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            return cnt
        for idx, word in enumerate(words):
            if is_one_letter_diff(cur, word) and not visited[idx] :
                queue.append((word, cnt+1)) 
                visited[idx] = True
    return 0