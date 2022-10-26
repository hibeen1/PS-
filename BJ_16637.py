import sys
input = sys.stdin.readline
max = -int(1e9)

def dfs(depth, result):
    if depth==len(operators):
        global max
        if max < result:
            max = result
        return

    if depth+1 < len(numbers):
        dfs(depth+1, calculate(result, numbers[depth+1], operators[depth]))
    if depth+2 < len(numbers):
        temp = calculate(numbers[depth+1], numbers[depth+2], operators[depth+1])

        dfs(depth+2, calculate(result, temp, operators[depth]))

def calculate(num1, num2, operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    else:
        return 0

n = int(input())
arr = input().strip()
numbers = []
operators = []
for i, item in enumerate(arr):
    if i%2==0:
        numbers.append(int(item))
    else:
        operators.append(item)
dfs(0, numbers[0])
print(max)
    