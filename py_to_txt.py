# -*- coding: utf-8 -*-
import os
import numpy as np

# 写入内容到txt中
num = np.arange(12).reshape((3, 4))
output_dir = os.path.dirname(__file__)
filename = os.path.join(output_dir, 'abc.txt')
with open(filename, "w") as f:
    for i in range(0, len(num)):
        f.write(str(num[i]) + "\n")
    f.close()

# 一起读取
fr = open(output_dir + '/abc.txt')
data = fr.read().splitlines()
print('一起读取：\n', data)

# 按行读取
lis = []
fr2 = open(output_dir + '/abc.txt')
for line in fr2.readlines():
    lis.append(line)
print('按行读取：\n', lis)
