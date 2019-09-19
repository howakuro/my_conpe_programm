#センター採点
#https://language-test-201603.contest.atcoder.jp/tasks/arc001_1
_ = input()
s = input()
count = [0, 0, 0, 0]
for c in s:
    count[int(c) - 1] += 1
print(max(count),min(count))
    
