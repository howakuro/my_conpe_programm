N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

satisfaction = 0
before = None
for i in range(N):
    num = A[i] - 1
    satisfaction += B[num]
    try:
        if A[i+1] - 1 == num + 1:
            satisfaction += C[num]
    except:
        pass
print(satisfaction)
