from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

tree_info = list(input().rstrip())
ans = 0
for i in range(len(tree_info)):
    if tree_info[i] == "R":
        continue
    q = deque()
    visited = [False for _ in range(n)]
    
    for j in tree[i]:
        if tree_info[j] == "R" and not visited[j]:
            print(j)
            visited[j] = True
            ans += 1
            q.append(j)
    while q:
        temp = q.popleft()
        if tree_info[temp] == "R" and not visited[temp]:
            print(temp)
            visited[temp] = True
            ans += 1
            q.append(temp)
print(ans)

    
