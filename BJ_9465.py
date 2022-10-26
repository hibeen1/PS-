import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    comp = [-1 for _ in range(n)]
    
    
