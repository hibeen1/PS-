import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()

start, end = 1, arr[k-1]
while True:
    if start > end:
        break
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)