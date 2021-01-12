def solution(A):
    if len(A) == 1:
        return A[0]
    max_end = max_slice = 0
#if all values are negative we simply return the largest among them. Because summing negative numbers will never lead to a number larger than the numbers themselves. 
    if max(A)<0:
        return max(A)
    for a in A:
        max_end = max(0, max_end + a)
        max_slice = max(max_slice, max_end)
    return max_slice