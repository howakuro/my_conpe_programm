import numpy as np
count = 0
N = int(input())
for k in range(2, N+1//2):
    n = N
    while n%k==0 and n > 1:
        n /= k
    if n % k == 1:
        count+= 1
print(count)
    

    
    