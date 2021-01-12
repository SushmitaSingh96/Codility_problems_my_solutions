def solution(A, K):
    # if no roation is needed or list is empty
    if K == 0 or A==[]:
        return A
    for _ in range(K):
        val = A.pop()
        A.insert(0,val)
    return A
    pass