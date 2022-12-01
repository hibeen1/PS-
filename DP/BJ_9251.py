# 풀이 보고 품
# https://myjamong.tistory.com/317

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
l1 = len(s1)
l2 = len(s2)
dp = [[0 for _ in range(l1)] for _ in range(l2)]

