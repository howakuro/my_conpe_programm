import numpy as np
N = int(input())
dp = np.zeros((N+1,3))
for i in range(N):
    happiness = list(map(int,input().split()))
    for j in range(3):#前日の行動
        for k in range(3):#今日の行動
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k],dp[i][j] + happiness[k])
print(int(max(dp[N])))