import copy as cp

#Eraクラス
class Era:
    """
    フィールド:
        now_era:int 現在の時代の番号
        era_eval:各時代の評価 "s" or "d"
        root:今まで通ってきた時代のルート
        cost:合計コスト
    """
    def __init__(self,now_era,era_eval,root,cost):
        self.now_era = now_era
        self.era_eval = era_eval
        self.cost = cost
        self.root = root
    
    def turn_era_eval(self,target_era):
        """
        target_era以降の時代の評価を反転
        引数:
            target_era:目的の時代
        """
        copy_era_eval = cp.deepcopy(self.era_eval)
        for i in range(target_era+1,N):
            copy_era_eval[i] = "s" if copy_era_eval[i] == "d" else "d"
        return copy_era_eval
    
    def append_root(self):
        """
        era.rootにそこに現在の時代を追加したcopy_rootを作成する
        返り値:copy_root
        """
        copy_root = cp.deepcopy(self.root)
        copy_root.append(self.now_era + 1)
        return copy_root
        
    def check_all_root(self):
        """
        root内に全ての時代が存在するか確認
        返り値:
            全てあった場合:True
            全て無かった場合:False
        """
        for i in range(N):
            if not(i+1 in self.root):
                return False
        return True
        
def timeslip(era):
    """
    最小コストの時代移動を探索する
    引数:
        era:現在の時代
    """
    global min_cost
    global min_root
    if min_cost < era.cost:#現在の時代のコストが既存の最小コストを超えてる場合打ち切り
        return
    if len(era.root) >= N and era.now_era == N-1:#N個以上の時代を周り、現在の時代に到達した場合
        #print(era.now_era,era.era_eval,era.cost,era.root)
        if era.check_all_root():#全時代が存在するかをチェック
            era.root = era.append_root()#現在の時代をera.rootに追加
            min_root = era.root if era.cost < min_cost else min_root#現在の時代のコストが最小コストならmin_rootへ
            min_cost = era.cost if era.cost < min_cost else min_cost#現在の時代のコストが最小コストならmin_costへ
        return
    #次に移動する時代を決定するループ
    for era_num,evaluate in enumerate(era.era_eval):#era_num:目的の時代, evaluate:目的の時代の評価
        if evaluate == "s" and era_num != era.now_era:#目的の時代の評価が安全かつ現在の時代ではない場合
            if era_num > era.now_era:#未来
                timeslip(Era(era_num, era.turn_era_eval(era_num),era.append_root(),era.cost + c_f))
            elif era_num < era.now_era:#過去
                timeslip(Era(era_num, era.turn_era_eval(era_num),era.append_root(),era.cost + c_b))


min_cost = float("inf") #今までの最小コスト
min_root = None #今までの最小コストのルート
N = int(input())#時代数
c_f,c_b = map(int,input().split())#c_f:未来の移動コスト c_b:過去の移動コスト
now_era = Era(N-1, list(input()),[], 0)#現在の時代
timeslip(now_era)
for i in min_root: 
    print(i,end=" ")#描画処理 