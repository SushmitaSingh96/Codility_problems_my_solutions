def solution(A, B, K):
    if A==B:
        if A==0:
            return 1
        elif K<A and (K%A == 0 or A%K==0) and A!=1:
            return 1
        elif K==A:
            return 1
        else:
            return 0
    for i in range(A, B+1):
        if i%K == 0:
            start = i//K
            break
    else:
        return 0
    mul = start*K
    if mul != B:
        end  = B//K
        return end-start+1
    else:
        return 1
    pass