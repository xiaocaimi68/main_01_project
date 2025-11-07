def xx(func):
    def a():
        #在执行原函数的触发
        print("准备开始")
        func()#被修饰的原函数
        #在执行原函数后触发
        print("执行结束")
    return a
@xx
def x():
    print("吃饭")

@xx
def y():
    print("睡觉")

if __name__=='__main__': 
    x()
    y()