from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
permu = permutations(li, m)
for i in permu:
    for j in i:
        print(j, end=" ")
    print()