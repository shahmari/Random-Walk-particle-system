import math as mt
import random as rm
import matplotlib.pyplot as plt 
y=4.9
g=-5
n=0
r=0.1
dt=0.03
x1=0
y1=0
xl=[]
yl=[]
def csn(x,y,r) :
    xr=round(x)
    yr=round(y)
    if mt.sqrt((x-xr)**2+(y-yr)**2)<=2*r :
        if (xr%2==0 and yr%2==0) or (xr%2==1 and yr%2==1) :
            o=1
        else :
            o=0
    else:
        o=0
    if y>2*r :
        o=0
    return(o)
def aht(x,y,x1,y1) :
    xr=round(x)
    yr=round(y)
    sqrt=mt.sqrt((x-xr)**2+(y-yr)**2)
    if sqrt==0 :
        return(x,y,x1f,y1f)
    cs=(x-xr)/(sqrt)
    sn=(y-yr)/(sqrt)
    x1p=-((x1*cs)+(y1*sn))
    y1p=(-x1*sn)+(y1*cs)
    x1f=(x1p*cs)-(y1p*sn)
    y1f=(x1p*sn)+(y1p*cs)
    y=y+(y1f*dt)
    x=x+(x1f*dt)
    return(x,y,x1f,y1f)
def pjn(x,y,x1,y1,xl,yl) :
    while y>=-12 and csn(x,y,r)==0 :
        x=x+(x1*dt)
        y1=y1+(g*dt)
        y=y+(y1*dt)
        if y<-5.5 :
            xl.append(x)
            yl.append(y)
    return(x,y,x1,y1,xl,yl)
while n<25000 :
    x=rm.uniform(-0.19,0.19)
    while y>=-12 :
        (x,y,x1,y1,xl,yl)=pjn(x,y,x1,y1,xl,yl)
        (x,y,x1,y1)=aht(x,y,x1,y1)
    y=4.9
    x1=0
    y1=0
    n=n+1
plt.hist2d(xl, yl, bins=(140, 50))
plt.show()