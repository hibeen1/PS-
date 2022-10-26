import sys
input = sys.stdin.readline

n = int(input())
apple_left = 0
for _ in range(n):
    stu_num, apple_num = map(int, input().split())
    apple_left += apple_num % stu_num
print(apple_left)