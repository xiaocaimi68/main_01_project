import numpy as np

def packages(data):
    data=np.array(data)

    # 求平均值
    avg = np.mean(data)
    abnormal = []
    normal=[]
    #大于80的为危险
    if np.max(data)>80:
        print("危险")

    for num in data:
        if num > avg:
            abnormal.append(num)
        else:
            normal.append(num)

    # 正确的字典写法（重点！！）
    result = {
        "危险":np.max(data),
        "异常值": abnormal,
        "正常值": normal,
        "平均值": float(avg),
        "最大值": int(np.max(data)),
        "最小值": int(np.min(data)),
        "方差": float(np.var(data))
    }

    return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(packages(data))