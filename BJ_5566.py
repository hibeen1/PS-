import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = []
m_list = []
for _ in range(n):
    n_list.append(int(input()))
for _ in range(m):
    m_list.append(int(input()))

cnt = 0;
idx = m_list[cnt];
while True:
    if idx >= n-1:
        break
    idx += n_list[idx]
    if idx >= n-1:
        break
    cnt += 1
    idx += m_list[cnt]

print(cnt+1)