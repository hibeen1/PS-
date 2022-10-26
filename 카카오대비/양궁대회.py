from copy import deepcopy
        
def solution(n, info):
    
    answer = [-1]
    max_diff = -1

    def dfs(n, apeach, lion, li, depth):
        nonlocal answer
        nonlocal max_diff
        if depth >= 11:
    
            if apeach >= lion:
                return

            if n > 0:
                li[10] += n
            
            if max_diff < lion-apeach or answer[0] == -1:
                max_diff = lion-apeach
                answer = li
            elif max_diff == lion-apeach:
                for i in range(10, -1, -1):
                    if li[i] > answer[i]:
                        answer = li
                        break
                    elif li[i] < answer[i]:
                        break
                    else:
                        continue
            return
        
        if n > info[depth]:
            li1 = deepcopy(li)
            li1[depth] = info[depth]+1
            dfs(n-(info[depth]+1), apeach, lion+(10-depth), li1, depth+1)
        
    
        li2 = deepcopy(li)    
        if info[depth] > 0:
            dfs(n, apeach+(10-depth), lion, li2, depth+1)
        else:
            dfs(n, apeach, lion, li2, depth+1)

    li = [0 for _ in range(11)]
    dfs(n, 0, 0, li, 0)
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))


# n	info	result
# 5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
# 1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
# 9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
# 10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]






"""
def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]


"""