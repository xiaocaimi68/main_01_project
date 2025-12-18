import random

# 生成随机数
def num(n=20):
    data=[random.randint(1,100) for i in range(n)]
    return data

if __name__=='__main__':
    data=num()
    print("随机数列表为(今日的包裹数为：",data)
