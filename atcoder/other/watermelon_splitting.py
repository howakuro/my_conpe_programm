#双子のスイカ割り
#https://language-test-201603.contest.atcoder.jp/tasks/abc025_b
N,A,B = map(int,input().split())
position = 0#-:West +:East
for i in range(N):
    s,d = input().split()
    d = int(d)
    if A <= d <= B:
        move = d
    elif d < A:
        move = A
    else:
        move = B
    position += move if s == "East" else -move

if position < 0:
    print("West",-position)
elif position == 0:
    print(0)
else:
    print("East",position)
    

