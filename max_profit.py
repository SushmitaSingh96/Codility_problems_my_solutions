def solution(A):
    if A == []:
        return 0
    max_end = max_slice = 0
    prev = A[0]
    for a in A:
        max_end = max(0, max_end+a-prev)
        max_slice = max(max_slice, max_end)
        prev = a
    return max_slice