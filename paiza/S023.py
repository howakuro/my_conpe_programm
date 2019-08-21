class Dice:
    def __init__(self,T,B,U,D,L,R):
        self.dice = [T,U,R,L,D,B]#{"T":T,"U":U,"R":R,"L":L,"D":D,"B":B}
        self.upper_surface = self.dice[0]
        self.count = 0
    
    def search(self,num):
        for i, dice_num in enumerate(self.dice):
            #print(num,dice_num)
            if num == dice_num:
                if i == 1:#U
                    #print("U",end="")
                    self.up()
                elif i == 2:#R
                    #print("L",end="")
                    self.left()
                elif i == 3:#L
                    #print("R",end="")
                    self.right()
                elif i == 4:#D
                    #print("D",end="")
                    self.down()
                elif i == 5:#B
                    #print("UU",end="")
                    self.up()
                    self.up()
                
    def up(self):
        self.dice[0], self.dice[1], self.dice[5], self.dice[4]= self.dice[1],self.dice[5], self.dice[4],self.dice[0]
        self.upper_surface = self.dice[0]
        self.count += 1
    
    def down(self):
        self.dice[1],self.dice[5], self.dice[4],self.dice[0] = self.dice[0], self.dice[1], self.dice[5], self.dice[4]
        self.upper_surface = self.dice[0]
        self.count += 1
    
    def right(self):
        self.dice[2],self.dice[5], self.dice[3], self.dice[0] = self.dice[0], self.dice[2], self.dice[5], self.dice[3]
        self.upper_surface = self.dice[0]
        self.count += 1
    
    def left(self):
        self.dice[0], self.dice[2], self.dice[5], self.dice[3] = self.dice[2],self.dice[5], self.dice[3], self.dice[0] 
        self.upper_surface = self.dice[0]
        self.count += 1
    
    def print_dice(self):
        #print(self.dice,self.count,self.upper_surface)
        print(self.count)
        
T,B,U,D,L,R= map(int,input().split())
N = int(input())
d = Dice(T,B,U,D,L,R)
for i in range(N):
    num = int(input())
    #print(num,end=" ")
    d.search(num)
d.print_dice()


