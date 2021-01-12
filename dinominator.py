def solution(A):
    N = len(A)
    tmp = []
    stack = []
    count = 0
    for i in A:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-1] != stack[-2]:
                tmp.append(stack.pop())
                tmp.append(stack.pop())
    if len(stack) == 0:
        return -1
    num = stack[-1]
    count+= len(stack)
    ind = -1
    for value in tmp:
        if value == num:
            count+= 1
    for index, val in enumerate(A):
        if val == num:
            ind = index
            break
    if count> N/2:
        return ind
    else:
        return -1