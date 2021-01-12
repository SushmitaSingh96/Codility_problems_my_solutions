def solution(X, Y, D):
    if X==Y:
        return 0
    n = (Y-X)//D
    rem = (Y-X)%D 
    if rem == 0:
        return n
    return n+1 
    pass