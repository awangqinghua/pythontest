#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-04-12 13:46
# @Author   :wangqinghua
# @File     : func.py
# @Software : PyCharm

for a in range(1,10):
    for b in range(1,a+1):
        print('%s*%s=%s'%(b,a,b*a),end='\t')
    print('')

aa=[5,15,78,6,48,32,15,9,24]
def bb(aa):
    count=len(aa)
    for a in range(0,count):
        for b in range(a+1,count):
            if aa[a]>aa[b]:
                aa[a],aa[b]=aa[b],aa[a]
    return aa
print(bb(aa))