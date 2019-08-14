import untangle

# 将文件解析成对象
obj = untangle.parse('p11/data.xml')
#获取l标签
obj.root.title.__dict__['l']


obj.root.body.p['name']
