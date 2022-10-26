import sys
input = sys.stdin.readline

# 문제
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5

# 17
# 12

# O(NK) + O(M) = 100억
# O(logN) 이하로 풀어야 함


# #시간초과 O(N)
# def solution(cmd, a, b):
#     if cmd == 1:
#         li[a-1] = b
#     elif cmd == 2:
#         print(sum(li[a-1:b]))
#     else:
#         print("입력값을 확인하세요")
#         return


# https://velog.io/@corone_hi/구간-트리-Segment-Tree-Python

def init_segment_tree(node, start, end):
    if start == end:
        tree[node] = li[start]
    else:
        tree[node] = init_segment_tree(node*2, start, (start+end)//2) + init_segment_tree(node*2+1, (start+end)//2 + 1, end)
    return tree[node]

def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sub_sum(node*2, start, (start+end)//2, left, right) + sub_sum(node*2+1, (start+end)//2 + 1, end, left, right)

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff

    if start != end:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2 + 1, (start+end)//2+1, end, idx, diff)

def solution(cmd, a, b):
    if cmd == 1:
        diff = b - li[a-1]
        li[a-1] = b
        update(1, 0, n-1, a-1, diff)
    elif cmd == 2:
        print(sub_sum(1, 0, n-1, a-1, b-1))

n, m, k = map(int, input().split())
li = []
tree = [0] * 3000000
for _ in range(n):
    li.append(int(input()))
init_segment_tree(1, 0, n-1)
for _ in range(m+k):
    cmd, a, b = map(int, input().split())
    solution(cmd, a, b)
