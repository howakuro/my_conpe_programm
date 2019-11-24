import numpy as np
N,K = map(int,input().split())
H = np.array(list(map(int,input().split())))
print(np.sum(H >= K))
