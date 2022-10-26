import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bridge = []
for _ in range(m):
    bridge.append(list(map(int, input().split())))
