# coding: utf-8
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def add_prop(group):
    births = group.births.astype(float)
    # 转化为浮点数后才能进行除法。
    group['prop']=births/births.sum()
    return group

def get_top1000(group):
    return group.sort_index(['births'], ascending=False)[0:1000]


if __name__ =="__main__":
    nameFile = pd.read_csv('D://DataAnalysis//names//yob1880.txt', names=['Username','sex','births'])
    print nameFile.groupby('sex').births.sum()
    # print nameFile.groupby('sex').sum()

    years = range(1880,2011)
    # 设置统计年度
    pieces = []
    columns =['Username','sex','births']
    for year in years:
        path = 'D://DataAnalysis//names//yob%d.txt' %year
        frame = pd.read_csv(path, names=columns)
        # 将文件读取到DataFrame中
        frame['year'] = year
        pieces.append(frame)
    summary = pd.concat(pieces,ignore_index=True)
    print type(summary),type(frame)
    # pd.concat 连接数据，将所有数据整合到单个DataFrame中
    # 参数ignore_index 可以忽略read_csv所返回的原始行号
    # print names,frame
    total_births = summary.pivot_table('births',index='year',columns='sex', aggfunc=sum)
    # DataFrame的pivot_table是数据透视表，birth是要显示的数据，rows是行，cols是列，aggfunc是方法
    total_births.tail()
    total_births.plot(title='first pandas pic')
    # plt.show()
    # 按照year和sex分组以后进行累加，并计算比例后新增加到每个分组
    boys= summary.groupby(['year','sex']).apply(add_prop)
    boys_top1000 = boys.apply(get_top1000)
