def solution(A):
    # if only one item exists in the list
    if len(A)==1:
        return A[0]
    A = sorted(A)
    for i in range(0,len(A),2):
        #if the odd number is the last item of the list
        if i == len(A)-1:
            return A[i]
        if A[i] != A[i+1]:
            return A[i]
    pass