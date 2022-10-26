n = int(input())
li = list(map(int, input().split()))
num = int(1e9)
for i in li:
    if i > 0:
        num = min(num, i)
while True:
    if num == 1:
        print(1)
    flag = True
    comp = li[0] % num
    for i in range(1, len(li)):
        if li[i]%num != comp:
            num -= 1
            flag = False
            break
    if flag:
        print(num)
        break