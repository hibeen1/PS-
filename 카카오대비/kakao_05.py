def update(r, c, value):
    cels[r-1][c-1]["value"] = value
    for x, y in cels[r-1][c-1]["merged_list"]:
        cels[x][y]["value"] = value

def update(value1, value2):
    global ROW
    global COLUMN
    global cels
    for i in range(ROW):
        for j in range(COLUMN):
            if cels[i][j]["value"] == value1:
                cels[i][j]["value"] = value2

def merge(r1, c1, r2, c2):
    cels[r2-1][c2-1]["value"] = cels[r1-1][c1-1]["value"]
    cels[r2-1][c2-1]["merged_list"].append([r1-1, c1-1])
    cels[r1-1][c1-1]["merged_list"].append([r2-1, c2-1])

def unmerge(r, c):
    for x, y in cels[r-1][c-1]["merged_list"]:
        cels[x][y]["merged_list"]


def solution(commands):
    ROW = 50
    COLUMN = 50
    answer = []
    cels = [[{"init":"EMPTY", "value":None, "merged_list":[]} * 50 ] for _ in range(50)]
    for command in commands:
        line = command.split()
        if line[0] == "UPDATE":
            if len(line) == 4:
                cels[r-1][c-1].append(value)
                

    return answer