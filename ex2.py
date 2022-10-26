from collections import deque

def solution(logs):
    dic_list = dict()
    answer = []
    for log in logs:
        pk, num, score = map(str, log.split())
        num = int(num)
        score = int(score)
        if pk in dic_list:
            dic_list[pk]['scores'][num-1] = score
            if dic_list[pk]['resolve'][num-1] == 0:
                dic_list[pk]['resolve'][num-1] = num
        else:
            resolve = [0 for _ in range(100)]
            scores = [0 for _ in range(100)]
            dic_list[pk] = dict()
            
            dic_list[pk] = {'resolve': resolve, 'scores': scores}
            dic_list[pk]['scores'][num-1] = score
            if dic_list[pk]['resolve'][num-1] == 0:
                dic_list[pk]['resolve'][num-1] = num
    q = deque()
    idx = sorted(dic_list)
    for pk in idx:
        cnt = 0
        sum = 0
        for k, v in enumerate(dic_list[pk]['resolve']):
            if v > 0:
                cnt+=1
                sum+=dic_list[pk]['scores'][k]
        dic_list[pk]['cnt'] = cnt
        dic_list[pk]['sum'] = sum
    for i in range(len(idx)-1):
        li1 = dic_list[idx[i]]
        if li1['cnt'] < 5:
            continue
        for j in range(i+1, len(idx)):
            flag = False
            li2 = dic_list[idx[j]]
            if li1['cnt'] == li2['cnt']:
                if li1['sum'] == li2['sum']:
                    for k in range(100):
                        if li1['scores'][k] != li2['scores'][k]:
                            break
                        if k == 99:
                            flag = True
            if flag:
                if q.count(idx[i]) == 0:
                    q.append(idx[i])
                if q.count(idx[j]) == 0:
                    q.append(idx[j])
            
    q_size = len(q)
    if q_size == 0:
        return "None"
    else:
        # answer = []
        for _ in range(q_size):
            answer.append(q.pop())
        return sorted(answer)
print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))
