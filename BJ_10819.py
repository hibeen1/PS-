import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr_per = list(permutations(arr))
ans = 0
for li in arr_per:
    temp_sum = 0
    for i in range(n-1):
        temp_sum += abs(li[i] - li[i+1])
    if temp_sum > ans:
        ans = temp_sum
print(ans)
    

