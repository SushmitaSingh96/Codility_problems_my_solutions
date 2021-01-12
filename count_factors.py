import math
def solution(N):
    result = 0
    n = math.sqrt(N)
    for i in range(1,int(n)+1):
        if N%i == 0:
            result+=2
    if int(n)*int(n) == N:
        return result+1-2
    return result