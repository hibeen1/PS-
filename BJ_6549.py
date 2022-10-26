import sys
input = sys.stdin.readline

while True:
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        break
    n = temp[0]
    li = temp[1:]
    
