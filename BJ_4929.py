import sys
input = sys.stdin.readline

def bin_search(num, target_list, start, end):
    if start > end:
        return False, -1
    mid = (start + end) // 2
    if num == target_list[mid]:
        return True, num
    elif num < target_list[mid]:
        return bin_search(num, target_list, start, mid-1)
    else:
        return bin_search(num, target_list, mid+1, end)
    
ans_list = []
while True:
    li1 = list(map(int, input().split()))
    if len(li1) == 1 and li1[0] == 0:
        break
    li2 = list(map(int, input().split()))
    li1 = li1[1:]
    li2 = li2[1:]
    crossing_points = []
    for i in li1:
        flag, num = bin_search(i, li2, 0, len(li2)-1)
        if flag:
            crossing_points.append(num)
    li1_point = 0
    li2_point = 0
    ans = 0
    if len(crossing_points) == 0:
        ans = max(sum(li1), sum(li2))
    else:
        for point in crossing_points:
            ans += max(sum(li1[li1_point:li1.index(point)]), sum(li2[li2_point:li2.index(point)]))
            li1_point = li1.index(point)
            li2_point = li2.index(point)
        ans += max(sum(li1[li1_point:]), sum(li2[li2_point:]))
    ans_list.append(ans)
for i in ans_list:
    print(i)
    

# li = [1,2,3,4,5,6,7]
# print(li.index(4))
# print(li[2:li.index(7)+1])