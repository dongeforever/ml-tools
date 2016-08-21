#!/bin/env python
# -*- coding: utf-8 -*-
import ThinFatData
import DecisionTree 


data = ThinFatData.createDataSet(num=100000,version=2)
DecisionTree.testFromDF(data)
