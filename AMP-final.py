import math as mt
import random as rm
import matplotlib.pyplot as plt 
y=4.9
g=-0.0478
r=0.14
dt=0.005
x1=0
y1=0
xl=[]
yl=[]
xll=[]
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
    while y>=-30 and csn(x,y,r)==0 :
        x=x+(x1*dt)
        y1=y1+(g*dt)
        y=y+(y1*dt)
        xl.append(x)
        yl.append(y)
    return(x,y,x1,y1,xl,yl)
n=0
while n<400 :
    x=rm.uniform(-0.29,0.29)
    while y>=-30 :
        (x,y,x1,y1,xl,yl)=pjn(x,y,x1,y1,xl,yl)
        (x,y,x1,y1)=aht(x,y,x1,y1)
    plt.plot(xl, yl,linewidth=0.4)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('Projection')
    xll.append(xl[len(xl)-1])
    y=4.9
    x1=0
    y1=0
    xl=[]
    yl=[]
    n=n+1
plt.show()
