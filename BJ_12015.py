import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for num in arr:
    if dp[-1] < num:
        dp.append(num)
    else:
        start = 0
        end = len(dp)
        while end > start:
            mid = (start + end) // 2
            if dp[mid] < num:
                start = mid + 1
            else:
                end = mid
        dp[end] = num
print(len(dp)-1)