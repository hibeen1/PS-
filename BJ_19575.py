import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num_li = []
a, b = map(int, input().split())
ans = a
for _ in range(n):
    a, b = map(int, input().split())
    ans = ans * x + a
    ans %= (10**9 + 7)
print(ans)