import sys
input = sys.stdin.readline

n = int(input())
deposit = list(map(int, input().split()))
j = int(input())
time = int(input())
for _ in range(time):
    total = sum(deposit)
    for i in range(n):
        deposit[i] += j*(deposit[i] / total)
print(deposit[0])