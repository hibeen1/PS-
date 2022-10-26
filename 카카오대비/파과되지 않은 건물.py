#100 * 100 * 250000 -> O(N*M*K)
# 누적합 이용 -> O(K + N*M)

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    d = [[0]*1003 for _ in range(1003)]
    # 변화량 테이블에 스킬 기록
    
    # 4K
    for v in skill:
        kind, r1, c1, r2, c2, degree = v
        if kind == 1: degree = -degree
        d[r1][c1] += degree
        d[r1][c2+1] -= degree
        d[r2+1][c1] -= degree
        d[r2+1][c2+1] += degree
    
    # 누적합 처리
    # N * M
    for i in range(1, n):
        for j in range(m):
            d[i][j] += d[i-1][j]
    
    for i in range(n):
        for j in range(1, m):
            d[i][j] += d[i][j-1]
    
    ans = 0
    # N * M
    for i in range(n):
        for j in range(m):
            if d[i][j] + board[i][j] > 0:
                ans += 1
    
    return ans