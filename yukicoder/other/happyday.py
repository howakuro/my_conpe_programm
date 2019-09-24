#HAPPY DAY
#問題URL:https://yukicoder.me/problems/492
count = 0
a = [31,28,31,30,31,30,31,31,30,31,30,31]
for month,day_num in enumerate(a):
    for day in range(day_num):
        str_day = str(day)
        try:
            day_two = int(str_day[1])
        except:
            day_two = 0
        if month == int(str_day[0]) + day_two:
            count += 1
print(count)