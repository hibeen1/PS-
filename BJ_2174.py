import sys
input = sys.stdin.readline
N_DIRECTION = ["N", "E", "S", "W"]
E_DIRECTION = ["E", "S", "W", "N"]
S_DIRECTION = ["S", "W", "N", "E"]
W_DIRECTION = ["W", "N", "E", "S"]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class robot:
    def __init__(self, num, x, y, direction):
        self.num = num
        self.x = x      
        self.y = y
        self.direction = direction

def rotate(cmd, d, cnt):
    idx = cnt % 4
    if cmd == "L":
        if idx != 0:
            idx = 4 + (cnt%4)*(-1)
    
    if d == "N":
        return N_DIRECTION[idx]
    elif d == "E":
        return E_DIRECTION[idx]
    elif d == "S":
        return S_DIRECTION[idx]
    elif d == "W":
        return W_DIRECTION[idx]

# test_case = int(input())
ans_list = []
# for tc in range(test_case):
a, b = map(int, input().split())
graph = [[0 for _ in range(a)] for _ in range(b)]
n, m = map(int, input().split())
opers = []
robots = []
for i in range(1, n+1):
    x, y, d = input().split()
    # [로봇 넘버, x, y, d]
    this_robot = robot(i, b-int(y), int(x)-1, d)
    robots.append(this_robot)
    graph[this_robot.x][this_robot.y] = this_robot.num
answer = "OK"
for _ in range(m):
    opers.append(list(input().split()))
for item in opers:
    num, cmd, cnt = item[0], item[1], item[2]
    num = int(num)
    cnt = int(cnt)
    if cmd == "L" or cmd == "R":
        robots[num-1].direction = rotate(cmd, robots[num-1].direction, cnt)
        continue
    elif cmd == "F":
        x = robots[num-1].x
        y = robots[num-1].y
        idx = N_DIRECTION.index(robots[num-1].direction)
        nx = x + dx[idx] * cnt
        ny = y + dy[idx] * cnt

        if nx >= 0 and nx < b and ny >= 0 and ny < a:
            has_crashed = False
            if nx == x:
                if ny > y:
                    for i in range(y+1, ny+1):
                        if graph[x][i] != 0:
                            has_crashed = True
                            answer = "Robot " + str(num) + " crashes into robot " + str(graph[x][i])
                            break
                else:
                    for i in range(y-1, ny-1, -1):
                        if graph[x][i] != 0:
                            has_crashed = True
                            answer = "Robot " + str(num) + " crashes into robot " + str(graph[x][i])
                            break
            elif ny == y:
                if nx > x:
                    for i in range(x+1, nx+1):
                        if graph[i][y] != 0:
                            has_crashed = True
                            answer = "Robot " + str(num) + " crashes into robot " + str(graph[i][y])
                            break
                else:
                    for i in range(x-1, nx-1, -1):
                        if graph[i][y] != 0:
                            has_crashed = True
                            answer = "Robot " + str(num) + " crashes into robot " + str(graph[i][y])
                            break
            if has_crashed:
                break
            robots[num-1].x = nx
            robots[num-1].y = ny
            graph[nx][ny] = num
            graph[x][y] = 0
        else:
            opponent = ""
            if nx < 0:
                for i in range(x-1, -1, -1):
                    if graph[i][y] != 0:
                        opponent = str(graph[i][y])
                        break
            elif nx >= b:
                for i in range(x+1, b):
                    if graph[i][y] != 0:
                        opponent = str(graph[i][y])
                        break
            elif ny < 0:
                for i in range(y-1, -1, -1):
                    if graph[x][i] != 0:
                        opponent = str(graph[x][i])
                        break
            elif ny >= a:
                for i in range(y+1, a):
                    if graph[x][i] != 0:
                        opponent = str(graph[x][i])
                        break
            if opponent == "":
                answer = "Robot " + str(num) + " crashes into the wall"
            else:
                answer = "Robot " + str(num) + " crashes into robot " + opponent
            break
ans_list.append(answer)
for i in ans_list:
    print(i)

