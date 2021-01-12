from collections import defaultdict

def solution(A):
    if A == []:
        return 0
    start = defaultdict(int)
    end = defaultdict(int)
    for index, val in enumerate(A):
        start[index] = index-val
        end[index] = index+val
    end_keys = sorted(end.values())
    start_keys = sorted(start.values())
    i = 0
    j = 0
    active = 0
    intersections = 0
    while i < len(start_keys):
        if start_keys[i] <= end_keys[j]:
            active+= 1
            intersections+= (active-1)
            i+=1
        else:
            j+=1
            active-=1
        if intersections > 10000000:
            return -1
    return intersections
    pass