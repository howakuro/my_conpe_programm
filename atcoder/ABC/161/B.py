N,M = map(int,input().split())
A = list(map(int,input().split()))
popu = 0
p = sum(A) / (4*M)

for num in A:
    if num >= p:
        popu += 1

if popu >= M:
    print("Yes")
else:
    print("No")