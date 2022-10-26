def solution(id_list, report, k):
    answer = []
    dic = dict()
    banned_id = []
    for id in id_list:
        dic[id] = [0]
    for r in report:
        a, b = r.split()
        if b not in dic[a]:
            dic[b][0] += 1
            dic[a].append(b)
    for id in id_list:
        if dic[id][0] >= k:
            banned_id.append(id)
    for id in id_list:
        cnt = 0
        for b in banned_id:
            if b in dic[id]:
                cnt += 1
        answer.append(cnt)
    return answer


# # 다른사람 풀이
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)