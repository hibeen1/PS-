import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for i in range(n):
    age, name = input().split()
    hq.append([-int(age), -i, name])
print(hq)
heapq.heapify(hq)
print(hq)
    # hq.append([int(age), i, name])
for _ in range(n):
    age, i, name = hq.pop()
    print(-age, name)
# for i in hq:
#     print(i[0], i[2])