
#实例
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 用户输入摄氏温度
 
# 接收用户输入
celsius = float(input('输入摄氏温度: '))
 
# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))
