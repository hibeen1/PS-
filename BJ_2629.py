import sys
input = sys.stdin.readline

def make_table(value, index):
    global n
    if dp[index][value] is True:
        return
    dp[index][value] = True
    if index == n:
        return
    make_table(value, index+1)
    make_table(value+stones[index], index+1)
    make_table(abs(value-stones[index]), index+1)

n = int(input())
stones = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

max_weight = sum(stones)
dp = [[False for _ in range(max_weight+1)] for _ in range(n+1)]
make_table(0, 0)
ans = []
for i in targets:
    if i > max_weight:
        ans.append("N ")
    else:
        if dp[n][i] is True:
            ans.append("Y ")
        else:
            ans.append("N ")
ans = "".join(ans)
print(ans)
