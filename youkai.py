#coding: UTF-8
import numpy as np
from math import exp, pi, sin


#解析解
def Analytical_solution(x , t):
    u = 0.0
    for n in range(10):     #Σの計算(n=1000)
        n2 = 2.0 * n        #2nの定義
        u = u + 1 / (n2 + 1.0) * exp(-pow(n2 + 1 , 2) * pi * pi * t) * sin(n2 + 1) * pi * x     #Σ内の計算
    u = 4 / pi * u          #Σの外と計算
    return u


#初期パラメータ
Div_x = 8       #xの分割数
Div_t = 128     #tの分割数

h = 1.0 / Div_x		#x軸の間隔
r = 1.0 / 2.0
k = 1.0 / Div_t	#t軸の間隔
t = 0.0		#時間

u = np.zeros((Div_x+1,Div_t+1))		#計算配列宣言


#初期時刻の計算
for i in range(1,Div_x):
	u[i][0] = 1.0


#陽解法によるその他時刻の計算
for j in range(Div_t):
    t = t + k       #tの更新
    print ("tj = {}の時，".format(t))
    x = 0.0
    for i in range(1,Div_x):
        x = x + h       #xの更新
        u[i][j+1] = r * (u[i+1][j] + u[i-1][j]) + (1.0 - 2.0 * r) * u[i][j]     #uの計算
        Ans = Analytical_solution(x,t)      #関数より解析解を取得
        print ("\t u{},j = {}\t(数値解)\t{}\t(解析解)".format(i,u[i][j+1] , Ans))     #表示