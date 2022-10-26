import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
start = min