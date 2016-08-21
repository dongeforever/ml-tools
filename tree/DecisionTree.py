#!/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import pandas as pd
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.externals.six import StringIO  
import pydot 
import subprocess as subps
import os

def test_and_report(full_x,full_y,columns):
    ''' 拆分训练数据与测试数据 '''
    x_train, x_test, y_train, y_test = train_test_split(full_x, full_y, test_size = 0.8)
    ''' 使用信息熵作为划分标准，对决策树进行训练 '''
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    print(clf)
    clf.fit(x_train, y_train)

    ''' 把决策树结构写入文件 '''
    export(clf)

    ''' 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大 '''
    print("features:")
    print(columns[:-1])
    print("feature_importances_:")
    print(clf.feature_importances_)
    '''准确率与召回率'''
    precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
    '''生成结果对比'''
    answer = clf.predict_proba(full_x)[:,1]
    print("answer vs full_y:")
    print(answer)
    print(full_y)
    print(classification_report(full_y, answer, target_names = columns[:-1].tolist()))

def export(clf):
    dot_file= 'dump/tree.dot'
    pdf_file= 'dump/tree.pdf'
    with open(dot_file,'w') as DOT_FILE:
        tree.export_graphviz(clf, out_file=DOT_FILE)
        DOT_FILE.close()
    command = 'dot -Tpdf ' + dot_file + ' -o ' + pdf_file + ''
    print command
    os.system(command)

    ''' 有bug，以后再来找问题
    dot_data = StringIO() 
    tree.export_graphviz(clf, out_file=dot_data) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_pdf("data/tree.pdf") 
    '''

def testFromDF(data):
    full_x = data.as_matrix()[:, :-1]
    full_y = data.as_matrix()[:, -1]
    test_and_report(full_x,full_y,data.columns.get_values())


