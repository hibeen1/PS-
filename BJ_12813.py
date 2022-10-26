import sys
input = sys.stdin.readline
# a = input().rstrip()
# b = input().rstrip()
a = int(input(), 2)
b = int(input(), 2)
ans = [[] for _ in range(5)]
# l = len(a)
l = 100000
mask = 2 ** l - 1
print(bin(a & b)[2:].zfill(l))
print(bin(a | b)[2:].zfill(l))
print(bin(a ^ b)[2:].zfill(l))
print(bin(a ^ mask)[2:].zfill(l))
print(bin(b ^ mask)[2:].zfill(l))

# for i in range(l):
#     ans[0].append(int(a[i]) & int(b[i]))

# for i in range(l):
#     ans[1].append(int(a[i]) | int(b[i]))

# for i in range(l):
#     ans[2].append(int(a[i]) ^ int(b[i]))

# for i in range(l):
#     ans[3].append(0 if int(a[i]) else 1)

# for i in range(l):
#     ans[4].append(0 if int(b[i]) else 1)

# for i in ans:
#     print()

