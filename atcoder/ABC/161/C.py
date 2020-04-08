N,K = map(int,input().split())
a = N % K 
print(min(abs(a - K),a))