import sys
from itertools import combinations
input = sys.stdin.readline

s_list = []
for _ in range(3):
    s_list.append(list(input().rstrip()))
k = int(input())
s_dic = {}
ans = set()

for i in s_list:
    combi = combinations(i, k)
    for j in combi:
        s = "".join(j)
        if s in s_dic.keys():        
            ans.add(s)
        else:
            s_dic[s] = 0
if len(ans) == 0:
    print(-1)
else:
    for i in sorted(ans):
        print(i)