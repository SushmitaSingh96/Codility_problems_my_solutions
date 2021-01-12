def solution(A):
    if len(A)==1:
        if A[0]==1:
            return 1
        else:
            return 0
    set_A = set(A)
    m = max(set_A)
    s = m*(m+1)//2
    if sum(set_A) != s:
        return 0
    d= dict.fromkeys(set_A, 0)
    for i in A:
        d[i]+=1
    for i in d.keys():
        if d[i] >1:
            return 0
    return 1
    pass