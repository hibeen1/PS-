import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = -1
def check(b, li, idx):
    for i, num in enumerate(b[idx:]):
        if num != li[i+idx]:
            return 0
    return 1
    

# 1. b 리스트에 a 리스트에 없는 값이 들어있는 경우 
if len(list(val for val in b if val not in a)) != 0:
    ans = 0
else:
    val = list(val for val in a if val not in b)
    if len(val) == 1:
        idx = a.index(val[0])
        li = sorted(a[:idx]) + a[idx:]
        temp = a[idx]
        while True:
            ans = check(b, li, idx)
            if ans == 1:
                break
            if idx == 0 or li[idx] > li[idx-1]:
                li[idx] = temp
                break
            li[idx] = li[idx-1]
            idx -= 1
    elif len(val) == 0:
        idx = n-1
        for i in range(1, n):
            if b[i] < b[i-1]:
                idx = i
                break
        li = sorted(a[:idx]) + a[idx:]
        ans = check(b, li, 0)
    else:
        ans = 0
print(ans)


            
                

# a = set([1,2,3,4,5])
# b = set([1,2,3,4,7])
# print(list(val for val in a if val not in b))
# print(list(val for val in b if val not in a))
# li = [3, 6, 2, 1, 8]
# print(sorted(li[:2]) + li[2:])