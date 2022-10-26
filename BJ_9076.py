import sys
input = sys.stdin.readline

answers = []
t = int(input())
NUM_OF_REFREE = 5
for _ in range(t):
    li = sorted(list(map(int, input().split())))[1:NUM_OF_REFREE-1]
    if li[len(li)-1] - li[0] >= 4:
        answers.append("KIN")
    else:
        answers.append(sum(li))
for answer in answers:
    print(answer)
