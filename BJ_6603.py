import sys
from itertools import combinations
input = sys.stdin.readline

arr_list = []
while True:
    temp = list(map(str, input().split()))
    if temp[0] == "0":
        break
    arr_list.append(temp)
for i in arr_list:
    arr = list(combinations(i[1:], 6))
    for j in arr:
        print(" ".join(j)) 
    print()



    
    
