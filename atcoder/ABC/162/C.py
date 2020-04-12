import fractions
K = int(input())
sum = 0
D = {}
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            if not (a+b+c in D) :
               D[a+b+c] = fractions.gcd(fractions.gcd(a,b),c)
            sum += D[a+b+c] 
print(sum)
