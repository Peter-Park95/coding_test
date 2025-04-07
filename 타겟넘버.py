def solution(numbers, target):
    answer = 0
    
    def calculator(total, count, idx):
        nonlocal answer
        if count == len(numbers):
            if total == target:
                answer += 1
        else:
            plus = total + numbers[idx]
            minus = total - numbers[idx]
            calculator(plus, count+1, idx+1)
            calculator(minus, count+1, idx+1)

    calculator(0,0,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))