S = list(input()) * 2
K = int(input())
Len_S2 = len(S)
Len_S1 = Len_S2 // 2
count1 = 0
count2 = 0
tmp = all(c == S[0] for c in S[:Len_S1:])
for i in range(Len_S2-1):
    if S[i] == S[i+1]:
        if i < Len_S1 - 1:
            count1 += 1
        if i < Len_S2:
            count2 += 1
        S[i+1] = "1"
diff = count2 - count1
if tmp and K >= 3 and Len_S1 % 2 != 0:
    print((count1 + (diff - 1) * (K-1)) + (1 * (K // 2)))
else:
    print(count1 + diff * (K-1))
