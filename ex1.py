def solution(v, a, b):
    answer = 0
    while True:
        print(v)
        answer += 1
        v = [v[i] - b for i in range(len(v))]
        v[0] += b-a
        max_v = max(v)
        min_v = min(v)
        if min_v < b or max_v < a:
            break
        idx = v.index(max_v)
        temp = v[0]
        v[0] = max_v
        v[idx] = temp
    return answer
print(solution([4, 5, 5], 2, 1))
print(solution([4, 4, 3], 2, 1))