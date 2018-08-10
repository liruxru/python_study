# 在python中 定义一个函数要用 def 关键字
def my_function(x):
    if not isinstance(x,(int, float)):
        raise TypeError("错误的参数")
    if x > 0:
        return x
    else:
        return -x


print(my_function(20))
print(my_function(-20))
print(my_function(-20.5))

# print(my_function("55"))


def power(x):
    return x * x
print(power(3))


def power(x, n):
    s=1
    if n == 0 :
        return 1
    while n > 0:
        s = s*x
        n = n-1
    return s

print(power(5,0))

# 使用默认参数
def power1(x, n=2):
    s=1
    if n == 0 :
        return 1
    while n > 0:
        s = s*x
        n = n-1
    return s
print(power1(5))