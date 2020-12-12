import numpy as np
from matplotlib import pyplot as plt
from numpy.random import *

M = 0.00 
M1 =  0.00 
goal = 100.00  
e = 0.00 
e1 = 0.00 
e2 = 0.00 
Kp = 0.8
Ki = 15


t = 1000

x_list = []
y_list = []

x_list.append(0)
y_list.append(0.00)

for i in range(1,t):
        M1 = M
        e2 = e1
        e1 = e
        e = goal - y_list[i-1] #偏差（e） = 目的値（goal） - 前回の操作量

        M = M1 + Kp * (e-e1) + Ki * e 

        x_list.append(i)
        y_list.append(M)

plt.hlines([goal], 0, t, "red", linestyles='dashed') #ゴールを赤色の点線で表示
plt.plot(x_list, y_list, color="b") #青色でグラフを表示
plt.ylim(0, goal*2) #グラフの高さを調整
plt.show()