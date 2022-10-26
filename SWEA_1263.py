tc = int(input())
ans_list = []
for t in range(tc):
    ans = -1
    temp = list(map(int, input().split()))
    n = temp[0]
    adj_mat = []
    start = 1
    for _ in range(n):
        adj_mat.append(temp[start:start+n])
        start += n
    dist = [[0 for _ in range(n)] for _ in range(n)]
    
    
        
        

    ans_list.append("#" + str(t) + " " + str(ans))