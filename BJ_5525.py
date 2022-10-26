n = int(input())
m = int(input())
s = input().rstrip()
i = 0
ans = 0
while True:
    if i >= m:
        break
    cnt = 0
    if s[i] == 'I':
        while True:
            if s[i+1:i+3] != 'OI':
                break
            cnt += 1
            i += 2
        if cnt >= n:
            ans += cnt-n + 1
    i += 1
print(ans)
