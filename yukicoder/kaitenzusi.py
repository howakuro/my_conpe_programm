#回転寿司
#問題URL:https://yukicoder.me/problems/78

"""memo = {}
def kaitenzusi(susi_number,before_get):
    if (susi_number,before_get) in memo:
        return memo[(susi_number,before_get)]
    if susi_number == N - 1:
        return V[susi_number]
    not_get = 0 
    if before_get == False:
        not_get = kaitenzusi(susi_number+1, True) + V[susi_number]
    get = kaitenzusi(susi_number+1, False)
    memo[(susi_number,before_get)] = not_get if not_get > get else get
    return memo[(susi_number,before_get)]"""

N = int(input())
V = [int(num) for num in input().split()]
dp = [0,]
dp1 = max(dp)
for i in range(N):
    pass

