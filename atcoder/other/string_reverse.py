#文字列の反転
#https://language-test-201603.contest.atcoder.jp/tasks/abc018_2
S = list(input())
N = int(input())
for i in range(N):
    l,r = map(int,input().split())
    S[l-1:r] = S[l-1:r][::-1]
print("".join(S))