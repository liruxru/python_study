# dict 字典 相当于map
d={"ly":85,"mike":70,"jack":87}
print(d)
# 索引必须为单引号
print(d['ly'])

# 这里单双引号都可以
print(d.get('mike'))
print(d.get("jack"))
# 如果key不存在 会返回none 或者指定的值 如 22
print(d.get("jack"),22)

# 删除一个
d.pop("mike")
print(d)

# 赋值添加
d["mark"]=66
print(d)
# 相同的key会覆盖
d["mark"]=99
print(d)


"""
set与dict类似,只存储键
"""
s=set(["ly","zm","mike","mike"])
print(len(s))
print(s)

s=set([1,1,2,2,3,3])
print(len(s))
print(s)

s.add("ly")
s.add("ly")
print(s)

# set做交集并集计算
s1=set([1,2,3])
s2=set([2,3,5])
print(s1&s2)
print(s1|s2)