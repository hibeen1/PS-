def solution(n, m, x, y, r, c, k):
    answer = ''

    # d l r u (하 좌 우 상)
    dlru = [["d", 0], ["l", 0], ["r", 0], ["u", 0]]
    dx = [1, 0, 0, -1] 
    dy = [0, -1, 1, 0]

    dist = abs(x-r) + abs(y-c)
    if dist > k or dist%2 != k%2:
        return "impossible"
    r_sum = r-x # + -> d, - -> u 
    c_sum = c-y # - -> l, + -> r 
    route = []
    route += "d"*r_sum if r_sum > 0 else "u"*abs(r_sum)
    route += "r"*c_sum if c_sum > 0 else "l"*abs(c_sum)
    route = "".join(sorted(route))

    dic = {}
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(nx < 1 or nx > n or ny < 1 or ny > m):
            dlru[i][1] += 1
    if 

        


    
    


    return answer


