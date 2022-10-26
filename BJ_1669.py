import sys
input = sys.stdin.readline

x, y = map(int, input().split())
dist = y-x
if dist == 0:
    print(0)
else:
    num = 1
    while True:
        n = int(num/2)
        temp = int(n*(n+1)/2)
        if num%2 == 0:
            temp *= 2
        else:
            temp = 2*temp + n+1
        if dist <= temp:
            break
        else:
            num+=1
    print(num)



    

        