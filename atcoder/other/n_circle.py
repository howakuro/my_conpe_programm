#N重丸
#https://language-test-201603.contest.atcoder.jp/tasks/abc026_b
import math
N = int(input())
R = [float(input()) for i in range(N)]
R.sort()
R.reverse()
area = 0.0
sign = 1.0
for i in range(len(R)):
    area += R[i] * R[i] * sign
    sign *= -1.0
print(area * math.pi)