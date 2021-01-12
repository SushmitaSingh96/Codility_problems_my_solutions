def solution(X, A):
    if len(A)==1 and X==1:
        return 0
    track = [0]*X
    store = [10000009]*X
    counter = 0
    for i, val in enumerate(A):
        if i<store[val-1]:
            store[val-1] = i
        track[val-1]=1
    if sum(track) == X:
        return max(store)
    return -1
    pass