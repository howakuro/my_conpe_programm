N = int(input())
h = list(map(int,input().split())) + [0] * 2
cost = [float("inf")] * (N+2)
cost[0] = 0
for i in range(N):
    cost[i+1] = min(cost[i+1], cost[i] + abs(h[i]-h[i+1]))
    cost[i+2] = min(cost[i+2], cost[i] + abs(h[i]-h[i+2]))
print(cost[N-1])
