# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    dic = {}
    for i in range(len(S)):
        if S[i] not in dic.keys():
            dic[S[i]] = []
        dic[S[i]].append(i+1)
    sections = []
    visited = []
    for value in dic.values():
        for i in range(len(value) - 1):
            sections.append([value[i], value[i+1]])
    visited = [False for _ in range(len(sections))]

    false_cnt = len(visited)
    answer = 0
    for idx in C:
        if false_cnt == 0:
            break
        answer += 1
        for i, section in enumerate(sections):
            if not visited[i]:
                if idx >= section[0] and idx < section[1]:
                    visited[i] = True
                    false_cnt -= 1
    if false_cnt > 0:
        return -1
    return answer