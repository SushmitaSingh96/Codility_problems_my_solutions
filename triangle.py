'''
If the array is sorted, you only have to check that the sum of two consecutive elements is greater than the next element (A[i] + A[i+1] > A[i+2]), 
because in that case, the other two conditions (A[i+1]+A[i+2] > A[i], A[i]+A[i+2] > A[i+1]) will always be true.
'''

def solution(A):
    if len(A) < 3:
        return 0

    A.sort()
    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0