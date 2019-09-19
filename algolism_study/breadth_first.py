from collections import deque
class Breadth_First_Search():
    """
    幅優先探索でsize*sizeのワールドの左上から右下を最短で繋ぐ経路を調べるクラス
        コンストラクタのパラメータ:
            size:int ワールドサイズ
    search:
        左下から右下を繋ぐ経路を調べるクラス
        引数:
            x:int x座標初期位置
            y:int y座標初期位置
    """
    def __init__(self,size):
        self.size = size
        self.count = 0
        self.root = []
    
    def search(self, x, y):
        q = deque([(x,y)])
        while q != deque([]):
            pos = q.popleft()
            print(q,"Pos:",pos)
            if pos[0] == self.size and pos [1] == self.size:
                self.count += 1
            if 0 <= pos[0] + 1 <= self.size:
                q.append((pos[0] + 1, pos[1]))
            if 0 <= pos[1] + 1 <= self.size:
                q.append((pos[0], pos[1] + 1))

if __name__ == "__main__":
    bfs = Breadth_First_Search(2)
    bfs.search(0,0)
    print("ルート数:",bfs.count)