import json

"""
    json只能使用双引号
"""
json_1 = '{"name":"尼古拉斯·赵四"}'
print(json_1)
print(type(json_1))

# 将json转化为字典格式
data = json.loads(json_1)
print(data)
print(type(data))

dict_1 = {"name": "尼古拉斯·赵四"}
# 将字典转化为json数据
res1 = json.dumps(dict_1, ensure_ascii=False)
print(res1)
print(type(res1))
