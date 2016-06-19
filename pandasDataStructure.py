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
df.index.name = "indexTest" # 指定DataFrame的索引名称
df.columns.name = "colTest"  # 指定DataFrame的列名称
# Result:
# colTest    one  Three  two
# indexTest
# 1          1.0    NaN    1
# 2          2.0    NaN    2
# 4          3.0    NaN    3
# 3          NaN    1.0    4
# ~~~~~~~~~~~~~~~总结~~~~~~~~~~~~~~~~~~~
# 可使用index和columns指定行序号和列序号,改行序号并不修改数据顺序，改列序号修改数据顺序

# ~~~~~~~~~~~DataFrame转换为其他类型~~~~~~~~~~
print df.to_dict(orient='dict')
print df.to_dict(orient='list')
print df.to_dict(orient='series')
#orient的参数包括'dict'、'list'、'series'和'records'
print df.head(),df.tail(),df.index
