# https://www.acmicpc.net/problem/11053
# DP or 이분탐색, LIS
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# dp = [1 for _ in range(n)]
# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

def binary_search(dp, x):
    start = 0
    end = len(dp) - 1
    while True:
        if start > end:
            break
        mid = (start + end) // 2
        if dp[mid] > x:
            end = mid - 1
        elif dp[mid] < x:
            start = mid + 1
        else:
            return mid
    return end + 1

dp = []
dp.append(arr[0])
for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        # idx = bisect.bisect_left(dp, arr[i])
        idx = binary_search(dp, arr[i])
        dp[idx] = arr[i]
print(len(dp))





# 6
# 10 20 10 30 20 50