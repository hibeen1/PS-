# [제약 사항]
# 1. 집의 개수 N은,  2 ≤ N ≤ 20 범위의 정수이다.
# 2. 집의 좌표 (x, y)는, -15 ≤ x, y ≤ 15 범위의 정수이다.
# 3. 각 집에서 충전소까지의 허용 가능한 거리 d는, 1 ≤ d ≤ 30 범위의 정수이다.


# [입력]
# 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스의 첫째 줄에는 N이 오고,
# 다음 N줄에는 집의 위치 x, y 그리고 각 집에서 충전소까지 허용 가능한 거리 d가 한 칸씩 공백을 두고 주어진다.


# [출력]
# 테스트 케이스의 결과는 "#C"를 찍고 한 칸 띄고 정답을 출력한다.
# (단, C는 테스트 케이스의 번호를 의미하며 1 부터 시작한다.)


# 5
# 2 
# -2 0 1
# 1 3 2
# 2 
# -1 -1 1
# 1 0 2
# 10 
# 3 5 4
# 2 6 8
# 7 4 10
# 6 6 11
# 3 3 3
# 5 2 8
# 0 5 10
# 4 7 9
# 6 2 5
# 1 1 10
# 5 
# -1 -2 1
# 4 -2 1
# 7 9 2
# 10 10 3
# 0 3 1
# 8
# 1 1 8
# -3 1 8
# -4 0 4
# 3 3 6
# -1 1 6
# -4 4 7
# -3 5 4
# -1 -2 4





from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def add_possible(x, y, dist, h):
    if dist == 0:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 31 and ny >= 0 and ny < 31 and not visited[nx][ny]:
            visited[nx][ny] = True
            graph[nx][ny].append(h)
            add_possible(nx, ny, dist-1, h)
T = int(input())
answer = []
for t in range(1, T+1):
    ans = -2
    n = int(input())
    homes = []
    graph = [[[] for _ in range(31)] for _ in range(31)]

    for i in range(n):
        x, y, dist = map(int, input().split())
        homes.append((abs(y-15), abs(x+15)))
        visited = [[False for _ in range(31)] for _ in range(31)]
        add_possible(homes[i][0], homes[i][1], dist, i)

    expected_positions = []
    points = []
    for i in range(31):
        for j in range(31):
            if len(graph[i][j]) == 0:
                continue
            if len(graph[i][j]) == n:
                points.append((i, j))
            if (i, j) not in homes:
                expected_positions.append((i, j))

    if len(points) > 0: # 충전소 한 대로 가능한 경우
        cnt = 1e9
        for point in points:
            temp = 0
            for home in homes:
                temp += abs(point[0] - home[0]) + abs(point[1] - home[1])
            cnt = min(cnt, temp)
        ans = cnt
    else:
        ep = list(combinations(expected_positions, 2))
        min_dist = 1e9
        for c in ep:
            first = c[0]
            second = c[1]
            if len(set(graph[first[0]][first[1]] + graph[second[0]][second[1]])) == n:
                dist = [1000000] * n
                for idx, home in enumerate(homes):
                    dist[idx] = min(abs(first[0]-home[0]) + abs(first[1]-home[1]), abs(second[0]-home[0]) + abs(second[1]-home[1]))
                min_dist = min(min_dist, sum(dist))
        ans = min_dist
        if ans == 1e9:
            ans = -1
    answer.append("#" + str(t) + " " + str(ans))
for ans in answer:
    print(ans)