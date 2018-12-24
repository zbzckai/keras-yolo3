# -*- coding: utf-8 -*-
# @Time    : 2018\12\24 0024 8:46
# @Author  : 凯
# @File    : transfrom_to_txt.py
import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'train_data\Annotations'
txtsavepath = 'train_data\ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('train_data\ImageSets/Main/trainval.txt', 'w')
ftest = open('train_data\ImageSets/Main/test.txt', 'w')
ftrain = open('train_data\ImageSets/Main/train.txt', 'w')
fval = open('train_data\ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
