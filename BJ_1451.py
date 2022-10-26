# 못 품

n, m = map(int, input().split())
rec = []
REC_SUM = 0
for i in range(n):
    rec.append(list(map(int, input())))
    REC_SUM += sum(rec[i])
print(REC_SUM)
answer = -int(1e9)
for x in range(n):
    for y in range(m):
        