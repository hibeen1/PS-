from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class macaron:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

def init_graph(li, graph):
    for i in range(5, -1, -1):
        if graph[i][li[0]-1] == 0:
            graph[i][li[0]-1] = macaron(i, li[0]-1, li[1])
            return graph[i][li[0]-1]

def bfs(macaron, graph):
    q = deque()
    li = []
    q.append(macaron)
    li.append(macaron)
    visited = [[False for _ in range(6)] for _ in range(6)]
    while len(q) > 0:
        m = q.pop()
        visited[m.x][m.y] = True
        for i in range(4):
            nx = m.x + dx[i]
            ny = m.y + dy[i]
            if nx >= 0 and nx < 6 and ny >= 0 and ny < 6:
                if not visited[nx][ny] and graph[nx][ny] != 0 and graph[nx][ny] == m.color:
                    q.append(graph[nx][ny])
                    li.append(graph[nx][ny])
    if len(li) >= 3:
        for i in li:
            graph[i.x][i.y] = 0
        return li
    return []


def update(graph):
    for i in range(6):
        while True:
            for j in range(4, -1, -1):
                graph[j+1][i] = graph[j][i]
                graph[j][i] = 0
            if graph[5][i] != 0:
                break
    return graph

def solution(macaron):
    answer = []
    graph = [[0 for _ in range(6)] for _ in range(6)]
    # 1. 떨어뜨리고 /  반복(2. 터지는 거 체크 3. 리맵)
    for i in macaron:
        temp = init_graph(i, graph)
        flag = bfs(temp, graph)    # 첫 번 째 돌리고 후보 리스트 반환
        graph = update(graph)
        if len(flag) > 0:
            q = deque()
            for i in flag:
                q.qppend(i)
            q_size = len(flag)
            while q_size > 0:
                for i in range(q_size):
                    flag = bfs(temp, graph)
                    for i in flag:
                        q.qppend(i)
                graph = update(graph)
                q_size = len(q)

    for i in range(6):
        str = ''
        for j in range(6):
            str += str(graph[i][j])
        answer.append(str)
    return answer

print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]))
