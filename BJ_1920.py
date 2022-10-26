# import sys
# input = sys.stdin.readline

# n = int(input())
# li1 = list(map(int, input().split()))
# m = int(input())
# li2 = list(map(int, input().split()))
# t1 = max(li1)
# t2 = max(li2)
# MAX = max(t1, t2)
# print(MAX)
# visited = [False for i in range(MAX+1)]
# for i in li1:
#     visited[i] = True
# for i in li2:
#     if visited[i]:
#         print(1)
#     else:
#         print(0)


import sys
input = sys.stdin.readline

n = int(input())
# n_list = sorted(list(map(int, input().split())))
n_set = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# def binary_search(start, end, target, n_list):
#     if start > end:
#         return 0
    
#     mid = (start + end) // 2
#     if target == n_list[mid]:
#         return 1
#     elif target < n_list[mid]:
#         return binary_search(start, mid-1, target, n_list)
#     else:
#         return binary_search(mid+1, end, target, n_list)

# for target in m_list:
#     print(binary_search(0, len(m_list)-1, target, n_list))

for i in m_list:
    print(1) if i in n_set else print(0)