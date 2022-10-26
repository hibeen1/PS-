import sys
input = sys.stdin.readline

def update_pigs(pigs):
    new_pigs = []
    # 나 왼 오 맞
    new_pigs.append(pigs[0] + pigs[1] + pigs[5] + pigs[3])
    new_pigs.append(pigs[1] + pigs[2] + pigs[0] + pigs[4])
    new_pigs.append(pigs[2] + pigs[3] + pigs[1] + pigs[5])
    new_pigs.append(pigs[3] + pigs[4] + pigs[2] + pigs[0])
    new_pigs.append(pigs[4] + pigs[5] + pigs[3] + pigs[1])
    new_pigs.append(pigs[5] + pigs[0] + pigs[4] + pigs[2])
    return new_pigs

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    pigs = list(map(int, input().split()))
    day_cnt = 1
    while True:
        if sum(pigs) > n:
            break
        day_cnt += 1
        pigs = update_pigs(pigs)
        print(pigs)
    ans.append(day_cnt)
for i in ans:
    print(i)
