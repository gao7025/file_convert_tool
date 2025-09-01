# -*- coding: utf-8 -*-
import os
import json

# 生成数据
num = list(range(4))
col = ['a', 'b', 'c', 'd']
data = dict()
for i in range(len(col)):
    data.update({col[i]: num[i]})

output_dir = os.path.dirname(__file__)
filename = os.path.join(output_dir, 'abc.json')

# 写入json格式文件
json_file = json.dumps(data)
with open(filename, "w") as f:
    f.write(json_file)
    f.close()

# 读取json格式文件
fr3 = open(output_dir + '/abc.json')
model = json.load(fr3)
for i in model.keys():
    print('key: %s   value: %s' % (i, model[i]))
