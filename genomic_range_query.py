def solution(S, P, Q):
    ans =[]
    if S == "":
        return 0
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        if 'A' in S[start: end+1]:
            ans.append(1)
        elif 'C' in S[start: end+1]:
            ans.append(2)
        elif 'G' in S[start: end+1]:
            ans.append(3)
        else:
            ans.append(4)
    return ans
    pass