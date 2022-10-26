import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
flag = cost[0]
idx = [0]
ans = 0
for i in range(1, len(cost)):
    if cost[i] < flag:
        flag = cost[i]
        idx.append(i)
    else:
        cost[i] = flag
if idx[-1] != n:
    idx.append(n)
for i in range(1, len(idx)):
    ans += cost[idx[i-1]]*sum(dist[idx[i-1]:idx[i]])
print(ans)

# temp = [1, 2, 3, 4, 5]
# print(sum(temp[0:5]))