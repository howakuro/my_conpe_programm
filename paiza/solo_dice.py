class Group():
    def __init__(self):
        self.member = []
        self.popularity = 0
    
    def add(self,people):
        self.member.append(people)
    
    def out(self,people):
        self.member.remove(people)
        
    def check_one_side_people(self,people1,people2):
        #print(people1,people2)
        if people1 in self.member and people2 in self.member:
            return False
        return True
            
    def culc_popularity(self):
        max_popularity = 0
        for key,value in friendry.items():
            if (key[0] in self.member or key[1] in self.member) and self.check_one_side_people(key[0],key[1]):
                max_popularity = value if max_popularity < value else max_popularity
        self.popularity = max_popularity
                
            
        
N,M,Q = map(int,input().split())
friendry = {}
for i in range(M):
    a,b,f = map(int,input().split())
    friendry[(a,b)] = f
#print(friendry)
g = Group()
for i in range(Q):
    op,q = input().split()
    q = int(q)
    if op == "+":
        g.add(q)
    else:
        g.out(q)
    g.culc_popularity()
    #print(g.member)
    print(g.popularity)