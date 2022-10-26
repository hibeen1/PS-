import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
ans = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(hq) == 0:
            # print(0)
            ans.append(0)
        else:
            # print(heapq.heappop(hq)[1])
            ans.append(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(cmd), cmd))
for i in ans:
    print(i)
