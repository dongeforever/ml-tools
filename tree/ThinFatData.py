#!/bin/env python
# -*- coding:utf-8 -*-
import random
import numpy as np
import pandas as pd
import json

def createDataSet(tall_range = None,weight_range = None, num = None,version=1):
    if tall_range == None:
        tall_range = [120, 200]
    if weight_range == None:
        weight_range = [40, 100]
    if num == None:
        num = 10000
    result = []
    for i in range(num):
        tall = random.randint(tall_range[0],tall_range[1])
        weight = random.randint(weight_range[0], weight_range[1])
        result.append((tall, weight, getClassValue((tall,weight),version)))
    df = pd.DataFrame(data=result, columns=['tall','weight','type'])
    return signType(df)

def signType(df):
    last_column = df.columns.get_values()[-1]
    #print last_column
    df = df.sort(last_column)
    '''巨坑，注意iloc与loc，sort不会改变索引的值'''
    value = df.iloc[len(df)/2][-1]
    #print value
    #print(df)
    df[last_column] = df[last_column].map(lambda x : 1 if x > value else 0)
    #print(df)
    return df

def getClassValue(X, version):
    if version == 1:
        return getClassValueV1(X)
    elif version == 2:
        return getClassValueV2(X)
    else:
        raise AssertError('unknown version:' + str(version))

'''线性关系'''
def getClassValueV1(X):
    return (X[0] - 60) * 0.65 -  X[1]

'''非线性关系'''
def getClassValueV2(X):
    tall = (X[0])/100.0
    tall2 = (X[0])/100.0
    BMI = X[1] / (tall*tall2)
    return BMI



    
if __name__ == '__main__':
    tt = createDataSet(version=2)
    print(tt)
    print 'num:%d positive:%d' % (len(tt),len(tt[tt.type == 1]))


        
