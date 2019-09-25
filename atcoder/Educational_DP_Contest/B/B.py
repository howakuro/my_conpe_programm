N, K = map(int,input().split())
h = list(map(int,input().split())) + [0] * K
cost = [float("inf")] * (N + K)
cost[0] = 0
for i in range(N):
    for j in range(1,K+1):
        cost[i+j] = min(cost[i+j], cost[i] + abs(h[i]-h[i+j]))
print(int(cost[N-1]))
