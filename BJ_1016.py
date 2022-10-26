MIN, MAX = map(int, input().split())
ans = MAX - MIN + 1
num_set = set()
start = 2
while True:
    if start**2 > MAX:
        break
    sq_num = start**2

    idx = MIN // sq_num if MIN%sq_num == 0 else (MIN // sq_num) + 1
    while True:
        if sq_num*idx > MAX:
            break
        num_set.add(sq_num*idx)
        idx += 1
    start += 1
ans -= len(num_set)
print(ans)
