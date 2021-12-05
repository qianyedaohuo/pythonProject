import requests

# user-agent :
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36

url = 'https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg'

hd = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
}

# 构造请求
response = requests.get(url, headers=hd)
# 查看状态码
print(response.status_code)
# 查看头部信息
print(response.headers)
# 查看源码
# print(response.text)
# 图片，音视频 得到二进制的文件内容
# print(response.content)

# with open('黑暗之女.png', 'wb') as f:
#     f.write(response.content)
