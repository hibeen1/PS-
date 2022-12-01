# 최소 신장 트리
# n <= 10만 -> O(nlogn) 이하

import sys
input = sys.stdin.readline

n = int(input())
coordinates = []
for _ in range(n):
    coordinates.append(list(map(int, input().split())))
