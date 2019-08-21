#A005:パイザボウルゲーム
a,b,n = map(int,input().split())
array = input().split()
count = 0
point = 0
scores = [0 if i == "G" else int(i) for i in array]
for i in range(len(scores)):
    if count == 0 and scores[i] == b:
        point += scores[i]
        try:
            point += scores[i + 1]
        except:
            pass
        try:
            point += scores[i + 2]
        except:
            pass
        count = 0
    elif count == 1 and scores[i-1] + scores[i] == b:
        point += scores[i]
        try:
            point += scores[i + 1]
        except:
            pass
        count = 0
    elif count == 1:
        point += scores[i]
        count = 0
    else:
        point += scores[i]
        count += 1
        
print(point)

        