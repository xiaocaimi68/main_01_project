from shuju import num
from shujufenxi import packages

def main():
    data=num(6)
    print(data)

    result=packages(data)

    print("分析结果:")
    for k, v in result.items():
        print(k, ":", v)


if __name__=="__main__":
    main()
