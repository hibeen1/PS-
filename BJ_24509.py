import sys
input = sys.stdin.readline

n = int(input())
score = []
ans = []
for _ in range(n):
    score.append(list(map(int, input().split())))
score.sort()
for i in range(1, 5):
    temp = max(score, key=lambda x: x[i])
    ans.append(temp[0])
    del score[score.index(temp)]
for i in ans:
    print(i, end=" ")