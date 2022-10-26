import sys
input = sys.stdin.readline

l = int(input())
r = 31
m = 1234567891
arr = input().rstrip()
num = 0
for i, v in enumerate(arr):
    num += (ord(v) - ord("a") + 1) * (r**i)
print(num%m)