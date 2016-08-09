#!/bin/env python
#-*- coding: utf-8 -*-
import math
import random

'''梯度下降法的样例，求f(x,y) = (x-40)^2 + (y-50)^2 的极小值'''


def getFxValue(args):
    return math.pow(args[0]-40, 2) + math.pow(args[1]-50, 2)

def nextArgs(args,step):
    '''分别求偏导，获取新的逼近点'''
    _x = args[0]
    _y = args[1]
    x = _x - step * (2 * (_x-40))
    y = _y - step * (2 * (_y-50))
    return (x,y)

def gradient_descent(x,y):
    #初始值
    args = (x,y)
    #步长
    step = 0.01
    #最大迭代次数
    N = 10000
    threshold = 0.00000000001
    last_value = 0xFFFFFFFF 
    n = 0
    while n < N:
        args = nextArgs(args,step)
        curr_value = getFxValue(args)
        change = math.fabs(curr_value - last_value)
        if change < threshold:
            return args
        last_value = curr_value
        n = n + 1

def test():
    print 'test'
    N = 100
    n = 0
    while n < N:
        x_init = random.randint(0,100)
        y_init = random.randint(0,100)
        res = gradient_descent(x_init, y_init)
        print x_init, y_init,res[0],res[1],getFxValue(res)
        n = n + 1
    


if __name__ == '__main__':
    test()

