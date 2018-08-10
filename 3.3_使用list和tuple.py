# 使用list
names = ["刘阳","东方国信","中煤科工"]
print(names)
# 获取list的大小
len = len(names)
print(len)
# 使用索引访问数据
print(names[0])
print(names[1])
print(names[2])

# IndexError: list index out of range print(names[3])

# 使用反向索引
print(names[-1]) # 倒数第一个
print(names[-2]) # 倒数第二个
print(names[-3]) # 倒数第三个

# list是可变的元素表 可以追加元素
names.append("admin")
names.append("mike")
print(names)
# 也可以把元素追加到指定位置
names.insert(1,"goods")
# 元素可以重复
names.append("mike")
print(names)

# 删除元素使用pop  使用索引或者不带参数删除最后一个
names.pop(0)
print(names)

# 将元素卸载参数里报错 names.pop("mike")

# 替换元素
names[0]="对不起"
print(names)

# list里的元素类型也可以不同
names.append(18)
print(names)


# 另一种有序列表叫元组 tuple 一旦初始化就不能修改
t = (1,2,2)
print(t)
# 只有一个元素,加逗号避免歧义
t = (3,)
print(t)