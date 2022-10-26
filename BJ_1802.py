import sys
input = sys.stdin.readline

def check_string(line):
    if len(line) < 1:
        return True
    flag = int(len(line)/2)
    left = list(line[:flag])
    right = list(line[flag+1:])
    right.reverse()
    for i in range(len(left)):
        if left[i] == right[i]:
            return False
    return check_string(left)

t = int(input())
for _ in range(t):
    line = input().rstrip();
    result = check_string(line)
    if result:
        print("YES")
    else:
        print("NO")


# temp = "01234"
# print(int(len(temp)/2))
# print(temp[:2])
# print(temp[3:])
# print(len(temp[:2]))
# print(len(temp[3:]))
