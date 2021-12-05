# file = open('./test.txt', 'w')
# file.write('hello world')
# file.close()
import os

path = './img/{}'
heroName = '黑暗之女'

if os.path.exists(path.format(heroName)):
    print('已经存在')
else:
    os.makedirs('./img/{}'.format(heroName))
    print('创建成功')
