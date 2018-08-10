names = ["liy","zhao","yang"]
for name in names:
    print(name)
for x in [1,2,.5,25,14,12]:
    print(x)

# range 生成 5到15 的整数 包头不包尾
ints = list(range(5,15))
for num in ints:
    print(num)

# 计算0-100的和
sum = 0
for x in range(101):
    sum+=x
print(sum)


# while循环
sum = 0
n = 99
while n > 0:
    sum+=n
    n = n - 2
print(sum)

for name in names:
    print("hello\t"+name)
