import pandas as pd
import numpy as np
import csv
import os
from pandas import DataFrame
os.chdir('C:\\Users\\luoliangkui\\Desktop\\20170927')
WIFI_TABLE = pd.read_csv('2017092701.csv',header=0)

#TEST
#print WIFI_TABLE.head()
# print WIFI_TABLE.columns
# print WIFI_TABLE['No.','RSSI'].head()

wifi =  WIFI_TABLE[['Time','source(un resovled)','RSSI']]
wifi_all = np.unique(wifi['source(un resovled)'])

#调试 显示筛选过一次的表
# print wifi_all
# df = DataFrame(wifi_all)
# df.to_csv('wifi_unique.csv',index=False)

#类似的结构
# print wifi.groupby(['source(un resovled)']).count().reset_index

# 输出表
wifi.to_csv('wifi_test1.csv',index=False)
