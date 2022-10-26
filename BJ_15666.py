# 중복조합

import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set(map(int, input().split()))
arr_combi = list(combinations_with_replacement(arr, m))
ans = list()
for i in arr_combi:
    ans.append(sorted(i))
for i in sorted(ans):
    print(*i, sep=" ")




