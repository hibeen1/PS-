# dic으로 할 건지 list로 할건지?

import math


def solution(fees, records):
    answer = []
    basic_tm, basic_fee, unit_tm, unit_fee = fees
    parking_info = {}
    fee_list = []
    
    for r in records:
        time, car_num, _ = r.split()
        if car_num not in parking_info.keys():
            parking_info[car_num] = []
        parking_info[car_num].append(int(time[:2])*60 + int(time[3:]))
        
    for key in parking_info.keys():
        if len(parking_info[key])%2 == 1:
            parking_info[key].append(23*60 + 59)
        in_time = parking_info[key][0::2]
        out_time = parking_info[key][1::2]
        t = 0
        t = sum(y-x for x, y in zip(in_time, out_time))
        fee = basic_fee
        if t > basic_tm:
            fee += math.ceil((t - basic_tm)/unit_tm)*unit_fee
        fee_list.append([key, fee])
    for info in sorted(fee_list):
        answer.append(info[1])
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))