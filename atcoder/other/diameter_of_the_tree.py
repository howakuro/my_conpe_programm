#高橋くんと木の直径
#https://language-test-201603.contest.atcoder.jp/tasks/abc019_4
class Tree():
    def __init__(self):
        self.node_number =  1

    #def create_node(self, node_number, dist_a, dist_b):

N = int(input())
for i in range(int(input())):
    a, b = map(int,input().split())
    
    a.append(a)
    b.append(b)

