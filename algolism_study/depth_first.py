#深さ優先探索
class Depse_First_Search():
    """
    深さ優先探索でsize*sizeのワールドの左上から右下を繋ぐ経路を調べるクラス
        フィールド:
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
        self.root.append((x, y))
        if x == self.size and y == self.size:
            self.count += 1
            print(self.count,self.root)
            return 
        if y < self.size:
            self.search(x, y + 1)
            self.root.pop()
        if x < self.size:
            self.search(x + 1 ,y)
            self.root.pop()

if __name__ == "__main__":
    dfs = Depse_First_Search(2)
    dfs.search(0,0)
    print("ルート数:",dfs.count)
    