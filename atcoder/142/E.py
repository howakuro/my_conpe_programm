import numpy as np
N,M = map(int,input().split())
keys = np.full(N,np.inf)
cost = []
for i in range(M):
    a,_ = map(int,input().split())
    c = map(int,input().split())
    check = False
    for j in c:
        if keys[j-1] > a:
            keys[j-1] = a
            check = True
print(cost)
if np.any(keys == np.inf):
    print(-1)
else:
    print(sum(cost))  


