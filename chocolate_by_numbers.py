def solution(N, M):
    if N == 1:
        return 1
    if M == 1:
        return N
    h = gcd(N,M,1)
    return int(N/h)

def gcd(a, b, res):
    if a==b:
        return res*a
    elif a%2 == 0 and b%2 == 0:
        return gcd(a//2, b//2, 2*res)
    elif a%2 == 0:
        return gcd(a//2, b, res)
    elif b%2 == 0:
        return gcd(a, b//2, res)
    elif a>b:
        return gcd(a-b, b, res)
    else:
        return gcd(a, b-a, res)