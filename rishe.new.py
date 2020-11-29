# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:14:54 2020

@author: alborz
"""


from math import cos,radians
def f(x):
    
    return x**2 +x -1


a=int(input("ebteday baze ra tayin konid:"))
b=int(input("entehaye baze ra tayin konid:"))
e=float(input("e:"))

l=b-a

while True:
    if (f(a)*f(b))<0:
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        elif f(b)*f(m)<0:
            a=m
        l=b-a
        if l<=e:
            print((a+b)/2)
            break
    else:
        print('there is no root for the function')
        break