import math
def comb(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N,M = map(int,input().split())
count = 0
if N <= 1:
    a = 0
else:
    a = comb(N,2)

if M <= 1:
    b = 0
else:
    b = comb(M,2)
print(a+b)

"""
偶+偶=偶
偶+奇=奇
奇+奇=偶
"""