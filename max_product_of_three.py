def solution(A):
    A.sort()
    np = 0
    if A[0]<0 and A[1]<0:
        np = A[0]*A[1]*A[-1]
    pp = A[-1]*A[-2]*A[-3]
    if pp>np:
        return pp 
    return np
    pass