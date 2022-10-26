import sys
input = sys.stdin.readline

def is_correct(a, b, oper, ans):
    if oper == "*":
        if ans == a*b:
            return True
    elif oper == "+":
        if ans == a+b:
            return True
    elif oper == "-":
        if ans == a-b:
            return True
    elif oper == "/":
        if ans == a//b:
            return True
    else:
        print("error")
    return False


t = int(input())
for _ in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[2])
    oper = line[1]
    ans = int(line[-1])
    if is_correct(a, b, oper, ans):
        print("correct")
    else:
        print("wrong answer")