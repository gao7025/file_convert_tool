# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd

# 生成数据
num = np.arange(12).reshape((3, 4))
col = ['a', 'b', 'c', 'd']
data = pd.DataFrame(num, columns=col)
output_dir = os.path.dirname(__file__)
# filename = os.path.join(output_dir, 'abc.txt')

# 写入CSV和Excel格式文件
data.to_csv(output_dir + '/abc2.csv', index=False)
data.to_excel(output_dir + '/abc2.xlsx', index=False, sheet_name='f1')

# 读取CSV和Excel格式文件
data2 = pd.read_csv(output_dir + '/abc2.csv')
print('csv格式：\n', data2)
data3 = pd.read_excel(output_dir + '/abc2.xlsx', sheet_name='f1')
print('excel格式：\n', data3)

# initial_file = pd.read_excel('D:/py_program/clients.xls', engine='xlrd', skiprows=[0], index_col=[0])

#
#
# # read json
# emb_filename = '/home/cqh/faceData/emb_josn.json'
# fr = open(emb_filename)
#
# model = json.load(fr)
# for i in model.keys():
#     print('key: %s   value: %s' % (i, model[i]))
#
# # write json
# import os
#
# name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': '4444'}
#
# output_dir = '/home/cqh/faceData'
# emb_filename = os.path.join(output_dir, 'emb_josn.json')
#
# jsObj = json.dumps(name_emb)
#
# with open(emb_filename, "w") as f:
#     f.write(jsObj)
#     f.close()
