import numpy as np
N,W = map(int, input().split())
dp = np.zeros((N+1,W+1), dtype=np.int64)
for i in range(N):
    w,v = map(int, input().split())
    for j in range(W):
        if j+w <= W:
            dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v) # 取る場合
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]) # 取らない場合
print(max(dp[N]))
