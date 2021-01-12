def solution(A, B):
    l = len(B)
    fishes = l
    if (sum(B) == l or (sum(B) == 0)):
        return l
    stack = []
    for i in range(l):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while len(stack):
                if stack[-1] > A[i]:
                    fishes-= 1
                    break
                if stack[-1] < A[i]:
                    fishes-= 1
                    stack.pop()
    return fishes
    pass