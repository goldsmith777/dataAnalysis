# coding: utf-8
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.util.testing as tm

nameFile = pd.read_csv('D://DataAnalysis//names//yob1880.txt', names=['Username','sex','births'])
print nameFile.groupby('sex').births.sum()
print nameFile[nameFile['sex']=='F'].shape,nameFile[nameFile['sex']=='M'].shape, nameFile.shape
newname = nameFile.pivot_table('births', rows='Username',cols='sex')
print newname['F']

