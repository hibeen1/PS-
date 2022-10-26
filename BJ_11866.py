import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
original = deque([x for x in range(1, n+1)])
josephus = "<"

# 방법 1. deque의 rotate(원형 큐 역할) 함수 활용
# for i in range(n):
#     original.rotate(len(original) - k + 1)
#     josephus += str(original.popleft()) + ", "

# 방법 2. 단순 무식 pop() append() 활용
for _ in range(n):
    idx = k - 1
    if len(original) < k:
        if k % len(original) == 0:
            idx = len(original) - 1
        else:
            idx = (k % len(original)) - 1
    for _ in range(idx):
        original.append(original.popleft())
    josephus += str(original.popleft()) + ", "


print(josephus[:-2] + ">")


