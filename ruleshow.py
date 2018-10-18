# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from recommendsystem.user_feature import *

data = loadData()
print data[0:1]
datas=[]
show=[]
counter={}

F = {}
B={}
a=0
item = {
        'click': 0,
       # 'rate': 0,
        'buy':0
    }

#F{}求每个产品的点击数目和购买次数
for uid, bid, action_type, month, day in data:
        F.setdefault(bid,copy(item))
        e=F[bid]
        if action_type == 0:
            e['click'] += 1
        elif action_type == 1:
            e['buy'] += 1

#datas将每个产品的点击数和购买数封装起来
for key in F:
    datas.append((F[key]['click'],F[key]['buy']))
print datas

#B相同点击数下的产品的购买次数,counter为相同点击数的产品的个数
for click,buy in datas:

    B.setdefault(click, 0)
    counter.setdefault(click,0)
    counter[click] += 1
    B[click] = B[click] + buy


#show计算相同点击数的平均购买率
for key in B:
    B[key]=B[key]/counter[key]
    show.append((key,B[key]))

#封装成dataframe
af= pd.DataFrame(show, columns=['click', 'rate'])
print af
x = af.click
y=af.rate
plt.bar(x,y,color='red')
plt.xlabel('click')
plt.ylabel('rate(%)')
plt.show()