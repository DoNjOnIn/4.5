import random as ran
import math as m
def shoot(x,y,r):
    p = m.sqrt((x + r) ** 2 + (y - r) ** 2)
    if r > p:
        print('ТАК')
    elif x>=0 and x<=2*r and y>-r and y<0:
        print('ТАК')
    else:
        print('НІ')
def main():
    r = float(input('R='))
    n=1
    while n<=10:
        x = float(input('x='))
        y = float(input('y='))
        shoot(x, y, r)
        n+=1
    n=1
    while n<=10:
        x = ran.uniform(-2*r, 2*r)
        y = ran.uniform(-2*r, 2*r)
        print('x='+str(round(x,2))+'    y='+str(round(y,2)))
        shoot(x, y, r)
        n+=1

if __name__=='__main__':
    main()
