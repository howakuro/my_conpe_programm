n = int(input())
R_min = float("inf")
R_max = -float("inf")
for i in range(n):
    R = int(input())
    R_max = max(R_max, R - R_min)
    R_min = min(R_min, R)
print(R_max)
