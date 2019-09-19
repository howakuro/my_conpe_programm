from collections import deque

def convert_bit(x):
    return bin(x).count("1")

N = int(input())
q = deque([(1,1)])
reach = [0 for i in range(N)]
empty = deque([])
while q != empty:
    node = q.popleft()
    if node[0] == N:
        print(node[1])
        exit()
    move = convert_bit(node[0])
    for m in [move,-move]:
        next_pos = m + node[0]
        if not 1 <= next_pos <= N:
            continue 
        if reach[next_pos - 1] == 0:
            q.append((next_pos,node[1] + 1))
            reach[node[0] - 1] = 1
print(-1)
  