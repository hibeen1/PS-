import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
gifts = list(map(int, input().split()))
children = list(map(int, input().split()))
ans = 1
heap = []
for i in gifts:
    heapq.heappush(heap, (-i, i))

for child in children:
    num, left_gift = heapq.heappop(heap)
    if left_gift < child:
        ans = 0
        break
    temp = left_gift-child
    heapq.heappush(heap, (-temp, temp))
print(ans)