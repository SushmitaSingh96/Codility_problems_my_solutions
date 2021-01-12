def solution(A):
    if A == []:
        return 1
    sA = sum(A)
    m = len(A)
    m+=1
    s = (m*(m+1))//2
    return s-sA
    pass