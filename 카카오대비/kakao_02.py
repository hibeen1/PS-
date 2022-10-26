def solution(cap, n, deliveries, pickups):
    answer = -1
    d_sum = sum(deliveries)
    p_sum = sum(pickups)
    d_idx = n
    p_idx = n
    while True:
        print(d_sum, p_sum)
        if d_sum == 0 and p_sum == 0:
            break
        d_cnt = cap
        p_cnt = cap
        for i in range(d_idx-1, -1, -1):
            if deliveries[i] > 0:
                if deliveries[i] > d_cnt:
                    deliveries[i] -= d_cnt
                    d_sum -= d_cnt
                    d_cnt = 0
                    d_idx = i
                else:
                    d_cnt -= deliveries[i]
                    d_sum -= deliveries[i]
            if d_cnt == 0 or d_sum == 0:
                break
        for i in range(p_idx-1, -1, -1):
            if pickups[i] > 0:
                if pickups[i] > p_cnt:
                    pickups[i] -= p_cnt
                    p_sum -= p_cnt
                    p_cnt = 0
                    p_idx = i
                else:
                    p_cnt -= pickups[i]
                    p_sum -= pickups[i]
            if p_cnt == 0 or p_sum == 0:
                break
        dist = 0
        if d_sum and p_sum:
            dist = max(d_idx, p_idx)
        else:
            if d_sum:
                dist = d_idx
            else:
                dist = p_idx
        answer += dist
    return answer

solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])