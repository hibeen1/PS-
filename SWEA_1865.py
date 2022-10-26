# import sys
# input = sys.stdin.readline


def search(prob, depth):
    global max_prob
    if prob < max_prob:
        return
    if depth == n:
        if False not in completed:
            max_prob = max(max_prob, prob)
        return
    
    for j in range(n):
        if prob_list[depth][j] == 0:
            continue
        if not completed[j]:
            completed[j] = True
            search(prob*prob_list[depth][j]/100, depth+1)
            completed[j] = False

t = int(input())
ans_list = []
for tc in range(t):
    max_prob = -1
    n = int(input())
    prob_list = []
    for _ in range(n):
        prob_list.append(list(map(int, input().split())))
    completed = [False for _ in range(n)]
    search(1, 0)
    ans_list.append("#" + str(tc+1) + " " +  format(round(max_prob*100, 6), ".6f"))
for i in ans_list:
    print(i)