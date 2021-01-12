'''
This is a mathematical problem... and to solve it you have to understand the relationship that exists between the averages of the slices.

We know from the problem description that the slices are a minimum length of 2. The trick to this problem is that the min average slice also cannot be longer than 3. So we only have to calculate the avg of the slices of length 2 and 3.
'''

def solution(A):
    index_pos = 0
    min_avg = (A[0]+A[1])/2
    for i in range(len(A)-2):
        tmp = (A[i]+A[i+1])/2
        if tmp < min_avg:
            min_avg = tmp
            index_pos = i
        tmp = (A[i]+A[i+1]+A[i+2])/3
        if  tmp < min_avg:
            min_avg = tmp
            index_pos = i
    tmp = (A[-1]+A[-2])/2
    if tmp < min_avg:
        index_pos = len(A)-2
    return index_pos
    pass