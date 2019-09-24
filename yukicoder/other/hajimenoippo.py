#はじめのn歩
#問題URL:https://yukicoder.me/problems/43
a,b = map(int,input().split())
walk = b/a
if b % a == 0:
    print(int(walk))
else:
    print(int(walk + 1))