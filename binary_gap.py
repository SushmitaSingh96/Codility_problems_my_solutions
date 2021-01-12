def solution(N):
    n = list(str(bin(N).replace("0b",""))[::-1])
    counts = []
    counter = 0
    flag = 0
    for i, val in enumerate(n):
        #print(val)
        if val == '1':
            flag = 1
            counts.append(counter)
            counter = 0
        elif val == '0' and flag==1:
            counter+=1
    return (max(counts))
