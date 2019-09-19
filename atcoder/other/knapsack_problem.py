#ナップサック問題
#https://language-test-201603.contest.atcoder.jp/tasks/abc032_d
N,W = map(int,input().split())
next_v,next_w = 0,0 
now_v,now_w = 0,0 
for i in range(N):
    v,w = map(int,input().split())
    if W > now_w + w:
        next_v,next_w = max(now_v + v, now_v)
    else:
        now_v,now_w = next_v,next_w

    
"""import random
import numpy as np
N = int(input())
a = np.random.choice(np.arange(10000),N)
next_dp = 0
dp = 0
for i in range(N):
    next_dp = max(dp, dp+a[i])
    dp = next_dp
print(dp)"""

