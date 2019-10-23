N = int(input())
count = 0
if N == 1:
    print(1)
else:
    for i in range(1,N+1):
        if i % 2 != 0:
            count += 1
    print(count/N)
