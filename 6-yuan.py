# 定义一个方法来计算圆的面积
def findArea(r):
    PI = 3.142
    return PI * (r*r)
 
# 调用方法
x=float(input('输入圆的半径：'))
print("圆的面积为 %.6f" % findArea(x))