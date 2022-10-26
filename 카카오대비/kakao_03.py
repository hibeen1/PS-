# 2^14 = 
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    dc_ratio = [10,20,30,40]
    emo_product_li = list(product(dc_ratio, repeat=len(emoticons)))
    for li in emo_product_li:
        tot_subscribers = 0
        tot_sales = 0
        for user in users:
            ratio_limit, tot_limit = user[0], user[1]
            tot = 0
            for i in range(len(li)):
                if li[i] >= ratio_limit:
                    tot += int(emoticons[i] * (100-li[i])/100)
            if tot >= tot_limit:
                tot_subscribers += 1
            else:
                tot_sales += tot
        answer = max(answer, [tot_subscribers, tot_sales])
    return answer
solution([], [])