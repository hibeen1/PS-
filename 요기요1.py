# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_num(stack1, stack2, stack3):
    li = []
    if len(stack1) > 0:
        li.append([stack1[-1], 1])
    if len(stack2) > 0:
        li.append([stack2[-1], 2])
    if len(stack3) > 0:
        li.append([stack3[-1], 3])
    res = max(li)
    if res[1] == 1:
        stack1.pop()
    if res[1] == 2:
        stack2.pop()
    if res[1] == 3:
        stack3.pop()
    return str(res[1])

def solution(stack1, stack2, stack3):
    n = len(stack1) + len(stack2) + len(stack3)
    answer = []
    for _ in range(n):
        answer.append(find_num(stack1, stack2, stack3))
    return "".join(answer)
