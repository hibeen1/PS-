# 1.진수 변환 함수
# 2. 0 제외 파싱 후 리스트에 append
# 3. 소수 판별 함수

from math import sqrt


def change_n(n, k):
    num = []
    while True:
        if n//k == 0:
            num.append(str(n))
            break
        num.append(str(n%k))
        n //= k
    print(num)
    return list(reversed(num))

def parsing_list(li):
    start = 0
    parsed_nums = []
    for i in range(len(li)):
        if li[i] == "0":
            if i != 0 and li[i-1] != "0":
                parsed_nums.append(int("".join(li[start:i])))
            start = i+1
    if start < len(li):
        parsed_nums.append(int("".join(li[start:])))
    print(parsed_nums)
    return parsed_nums


def is_prime_num(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(sqrt(num)) + 1):
        print(i, num)
        if num%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    li = change_n(n, k)
    parsed_nums = parsing_list(li)
    for num in parsed_nums:
        if is_prime_num(num):
            answer += 1
    return answer

print(solution(524287,2))




