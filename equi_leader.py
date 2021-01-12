def solution(A):
    leader = sorted(A)[len(A)//2]
    total = 0
    l = len(A)
    for i in A:
        if i == leader:
            total+= 1
    count = 0
    equi = 0
    for index, value in enumerate(A):
        if value == leader:
            count+=1
        l1 = index+1
        l2 = l - l1
        if count>l1//2 and (total-count)>l2//2:
            equi+=1
    return equi
