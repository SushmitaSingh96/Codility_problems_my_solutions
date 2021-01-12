def solution(A):
    if len(A)==1:
        return A[0]
    slice1 = A[0]
    slice2 = sum(A[1:])
    s = 10000009
    for i in range(1,len(A)):
        tmp = abs(slice1 - slice2)
        if tmp < s:
            s = tmp
        slice1 = slice1 + A[i]
        slice2 = slice2 - A[i]
    return s
    pass