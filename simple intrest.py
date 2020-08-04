
from datetime import datetime, date


def sim_int(a, r, c):
    y = a // 365
    m = (a-(y*365))//30
    d = (a-((y*365)+(m*30)))
    yr = y*12*r
    mr = m*r
    dr = (r/30)*d
    x = yr+mr+dr
    print(y, m, d)
    return x


def leep_year(y1,y2,m1,m2):
    count = 0
    if m1 <= 2 and m2 < 2:
        for i in range(y1,y2):
            if i%4==0:
                count= count+1
    elif m1 <= 2 and m2 >= 2:
        for i in range(y1,y2+1):
            if i%4==0:
                count= count+1
    elif m1 > 2 and m2 < 2 :
        for i in range(y1+1,y2):
            if i % 4 == 0:
                count = count + 1
    elif m1 > 2 and m2 >= 2:
        for i in range(y1+1,y2+1):
            if i % 4 == 0:
                count = count + 1
        print(count)
    return count


t = float(input('Enter total amount taken:'))
r = float(input('Enter the rate of interest:'))
d1 = input("Start date:")
d2 = input("End date:")
ys = int(d1.split('-')[0])
ye = int(d2.split('-')[0])
ms = int(d1.split('-')[1])
me = int(d2.split('-')[1])
x = leep_year(ys,ye,ms,me)
start = datetime.strptime(d1, "%Y-%m-%d")
end = datetime.strptime(d2, "%Y-%m-%d")
no_days = end - start
rt=(t/100)*r
print(no_days)
d = sim_int(no_days.days, rt,x) + t
print(d)