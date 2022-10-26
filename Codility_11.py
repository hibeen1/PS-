def solution(A):
    # write your code in Python 3.6
    A = sorted(list(filter(lambda x : x > 0, set(A))))
    ans = 0
    if len(A) == 0:
        print(1)
        return
        
    for i in range(1, len(A)):
        if A[i] != A[i-1]+1:
            ans = A[i-1] + 1
            break
    if ans == 0:
        print(max[A] + 1)
    else:
        print(ans)
A = [-1, 3]
solution(A)

a = [-1, -3]
print(sorted(list(filter(lambda x : x > 0, set(a)))))