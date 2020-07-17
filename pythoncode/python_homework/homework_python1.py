#this is homework for python1

#定义有参数的函数,下面函数的参数为必需参数
def have_arg(a):
    b = a+1
    #有返回值 返回值为b
    return b

#定义无参数的函数
def no_arg():
    print("this is no argument function")
    #无返回值情况 默认返回值为None
    return


print(have_arg(1))
#输出值为2

print(no_arg())
#输出值为“this is no argument”
# None