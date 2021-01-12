def solution(N, A):
    counters = [0]*N
    current_max = 0
    m = 0
    for i in A:
        if i<N+1:
            if counters[i-1]<m:
                counters[i-1] = m
            counters[i-1]+=1
            if current_max < counters[i-1]:
                current_max = counters[i-1]
        else:
            m = current_max   
    for i in range(N):
        if counters[i]<m:
            counters[i]=m
    return counters
    pass