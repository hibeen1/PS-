import sys

# 0~9, null
num_li = [  
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [1,0,1,1,0,1,1],
    [0,1,1,1,0,1,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [1,1,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0]
]

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a_li = []
    b_li = []
    cnt = 10000
    while True:
        if cnt < 1:
            break
        a_li.append(num_li[10] if a//cnt == 0 else num_li[int((a//cnt)%10)])
        b_li.append(num_li[10] if b//cnt == 0 else num_li[int((b//cnt))%10])
        cnt /= 10
        cnt = int(cnt)
    ans = 0
    for i in range(len(a_li)):
        for j in range(len(a_li[0])):
            ans += a_li[i][j] ^ b_li[i][j]
    print(ans)
