import math
import sys
input = sys.stdin.readline

def is_number(c):
    if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True
    return False

n = int(input())
arr = input()
i = 0
ans = 0

while True:
    # print(i)
    if i >= n:
        break
    if is_number(arr[i]):
        num = [int(arr[i])]
        while True:
            print(i)
            i += 1
            if not is_number(arr[i]):
                break
            num.append(int(arr[i]))
        for i in num:
            ans += i * 10^(len(num) - i-1)
        continue
    i += 1
print(ans)

            
        

