#ref document link for time complexity
def solution(A):
    A.sort()
    if A[len(A)-1]<0:
        return 1
    for i, val in enumerate(A):
        if val>0:
	#in operator is faster for set so we keep new_A as set not list
            new_A = set(A[i:])
            break
    start = 1
    end = A[-1]
    while (start<=end):
        if start in new_A:
            start+=1
        else:
            return start
    return start
    pass