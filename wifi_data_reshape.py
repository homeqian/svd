# coding=utf-8
import pandas as pd
import numpy as np
import csv
import os
import re
import matplotlib
from pandas import DataFrame
os.chdir('C:\\Users\\luoliangkui\\Desktop\\20170927')
WIFI_TABLE = pd.read_csv('2017092701.csv',header=0)

# TEST
# print WIFI_TABLE.head()
# print WIFI_TABLE.columns
# print WIFI_TABLE['No.','RSSI'].head()

wifi =  WIFI_TABLE[[u'Time',u'source(un resovled)',u'RSSI']]
wifi2 = wifi.copy()
# len(wifi)
for x in range(len(wifi2)):
    wifi2[u'RSSI'][x]=wifi2[u'RSSI'][x].rstrip(' dBm')
# print wifi2
# wifi2.to_csv('wifi_2.0.csv',index=False)

# print wifi2.dtypes
# wifi[u'RSSI']=wifi [u'RSSI'].astype('float64')
# wifi_all = np.unique(wifi['source(un resovled)'])

# 显示筛选过一次的表
# print wifi_all
# df = DataFrame(wifi_all)
# df.to_csv('wifi_unique.csv',index=False)

# 类似的结构
# print wifi.groupby(['source(un resovled)']).count().reset_index

# 输出表
# wifi.to_csv('wifi_test3.csv',index=False)

#from dataframe to dict

#构造字典集key为MAC地址 value值为其时间信息
mydict = {}
for x in range(len(wifi2)):
    currentid = wifi2.iloc[x,1]
    currentvalue = wifi2.iloc[x,0] + wifi2.iloc[x,2]
    mydict.setdefault(currentid,[])
    mydict[currentid].append(currentvalue)

with open('mycsvfile.csv','wb') as csv_file:
    # w = csv.DictWriter(csv_file,mydict.keys())
    # w.writeheader()
    # w.writerow(mydict.keys())
    writer = csv.writer(csv_file)
    # writer.writerow(mydict.keys())
    writer.writerows(mydict.values())

# df2 = pd.read_csv('mycsvfile.csv',header=0)
# print df2
# 输出事例
# print mydict
# print mydict['00:ec:0a:c8:6d:ef']
# 写入csv（errir）
