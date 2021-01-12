def solution(A):
    sum_all = sum(A)
    count = 0
    res = []
    flag = 0
    for val in A:
        if val == 0:
            flag=1
            res.append(sum_all - count)
        elif flag==1:
            count+=1
        else:
            count+=1
    ans = sum(res)
    if ans>1000000000:
        return -1 
    else:
        return ans