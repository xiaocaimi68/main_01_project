import numpy as np

x = [10, 25, 8, 40, 15, 60, 5, 100]
x = np.array(x)
print("原数组:",x)

#求平均
avg = x.mean()
print("平均值:",avg)

#找出异常值
abnormal=[]
normal=[]

for num in x:
    if num>avg:
        abnormal.append(num)
    else:
        normal.append(num)

        print("异常值:",abnormal)
        print("正常值:",normal)
        print("平均值:",avg)
        print("最大值:",x.max())
        print("最小值:",x.min())

#简单归一化处理
Y=x/np.max(x)
print("归一化处理后的数据:",Y)