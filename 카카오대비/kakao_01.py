def solution(today, terms, privacies):
    answer = []
    td_y = int(today[:4])
    td_m = int(today[5:7])
    td_d = int(today[8:])
    term_dic = {}
    for term in terms:
        a, b = term.split()
        term_dic[a] = int(b)*28
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:])
        cnt = (td_y - y)*12*28 + (td_m - m)*28 + (td_d - d)
        if term_dic[term] - cnt <= 0:
            answer.append(idx+1)
    return answer