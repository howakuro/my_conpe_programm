#一変数方程式
#https://language-test-201603.contest.atcoder.jp/tasks/tricky_2
import math
T = int(input())
for i in range(T):
    a, b, c = map(float,input().split())
    D = b*b - 4*a*c
    if D > 0:
        D = math.sqrt(D)
        N = 2
        answer1 = ((-b) + D) / (2*a)
        answer2 = ((-b) - D) / (2*a)
    elif D == 0:
        N = 1
        answer1 = (-b) / (2*a)
        answer2 = ""
    else:
        N = 0
        answer1 = ""
        answer2 = ""
    print(N,answer1,answer2)