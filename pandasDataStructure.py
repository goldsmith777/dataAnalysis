#coding: utf-8
import pandas as pd
import numpy as np


# DataFrame是二维的数据结构，本质是Series的容器. 即DataFrame的每一列可以是一个Series
# DataFrame可以包含一个索引以及与索引联合在一起的Series

#~~~~~~~~~~~~~~ 创建DataFrame ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %%%% 方法1.以列表的字典，或Series的字典，来构造DataFrame，eg：%%%%%%
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'd', 'c'])}
# 缺省的index是0,1,2,3...
e = {'one': [4,3,2,1], 'two': [1., 2., 3., 4.]}
# 使用列表的字典来构造DataFrame,需要保持每个列表元素数量相同
print pd.DataFrame(d)
print pd.DataFrame(e, index=['2','0','1','3'], columns=['two','one'])
# Result:
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  4.0
# d  NaN  3.0
# %%%%%% 方法2.从字典的列表构建DataFrame，其中每个字典代表的是每个记录,eg: %%%%%%
f =  [{'one' : 1,'two':1},{'one' : 2,'two' : 2},{'one' : 3,'two' : 3},{'two' : 4,'Three':1}]
# 使用这种方式，如果不通过columns指定列的顺序，那么列的顺序会是随机的，可使用下方法指定
df = pd.DataFrame(f,index=['1','2','4','3'],columns=['one','Three','two'])
# 可使用index和columns指定行序号和列序号,改行序号并不修改数据顺序，改列序号修改数据顺序
df.index.name = "indexTest" # 指定DataFrame的索引名称
df.columns.name = "colTest"  # 指定DataFrame的列名称
# Result:
# colTest    one  Three  two
# indexTest
# 1          1.0    NaN    1
# 2          2.0    NaN    2
# 4          3.0    NaN    3
# 3          NaN    1.0    4

# ~~~~~~~~~~~DataFrame转换为其他类型~~~~~~~~~~
# orient的参数包括'dict'、'list'、'series'和'records'
df.to_dict(orient='dict')
df.to_dict(orient='list')
df.to_dict(orient='series')

# head和tail方法可以显示DataFrame前N条和后N条记录，N的默认值为5.
print df.head(),df.tail()
# describe方法可以计算各个列的基本描述统计值,包括平均数、计数、最大、最小、标准差等
print df.describe()
# Result：
# colTest  one  Three       two
# count    3.0    1.0  4.000000
# mean     2.0    1.0  2.500000
# std      1.0    NaN  1.290994
# min      1.0    1.0  1.000000
# 25%      NaN    NaN  1.750000
# 50%      NaN    NaN  2.500000
# 75%      NaN    NaN  3.250000
# max      3.0    1.0  4.000000
print df.T.describe()
# Result：
# indexTest    1    2    4        3
# count      2.0  2.0  2.0  2.00000
# mean       1.0  2.0  3.0  2.50000
# std        0.0  0.0  0.0  2.12132
# min        1.0  2.0  3.0  1.00000
# 25%        NaN  NaN  NaN      NaN
# 50%        NaN  NaN  NaN      NaN
# 75%        NaN  NaN  NaN      NaN
# max        1.0  2.0  3.0  4.00000

# DataFrame提供多种排序方式
# 方式一：按照轴标签进行排序
print df.sort_index(axis=1, ascending=False)
# sort_index可以以轴的标签进行排序。axis是指用于排序的轴，可选的值有0和1，默认为0即行标签（Y轴），1为按照列标签排序。
# ascending是排序方式，默认为True即降序排列。
# 方式二：按照指定列进行排序


