# import sys
# input = sys.stdin.readline

# t = int(input())
# ans_list = []
# for _ in range(t):
#     ans = 0
#     s, f = map(int, input().split())
#     num = s
#     for i in range(s+1, f+1):
#         num = num ^ i
#         print(num)
#     ans_list.append(num)
# for i in ans_list:
#     print(i)



print(9, bin(9))
print(13, bin(13))
print(17, bin(17))
print(20, bin(20))
print(9^13, bin(9^13))
print(9^13^17, bin(9^13^17))
print(4^17, bin(4^17))
print(21^20, bin(21^20))
print(9^13^17^20, bin(9^13^17^20))
print(3^4^5^6^7^8^9^10)