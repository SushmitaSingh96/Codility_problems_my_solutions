import math as m

def solution(N):
    peri = []
    for i in range(1,int(m.sqrt(N)+1)):
        if N%i == 0:
            a = N//i
            peri.append(2*(a+i))
    return min(peri)