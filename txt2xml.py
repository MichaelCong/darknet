#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import sys
sys.path.append('/raid/rencong/yuhangcv')
from tqdm import tqdm
import yuhangcv
from pascal_voc_writer import Writer

###将txt格式文件转换为xml格式文件
# 图像存储位置
src_img_dir = "/home/rencong/ljjj/train/JPEGImages/"
# 图像的 ground truth 的 txt 文件存放位置
#windows 系统路径用“\”,ubuntu 中用“/”
src_txt_dir = "/raid/rencong/darknet/txt"
src_xml_dir = "/raid/rencong/darknet/xml"
#glob 返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。
img_Lists = yuhangcv.find(src_img_dir,['.jpg'])
img_file2path = {os.path.basename(file)[:-4]:file for file in img_Lists}

img_names = []  # 对应的是路径中的图像名字
for item in tqdm(img_Lists):
    #获取对应路径下文件的名字：os.path.basename
    img_names.append(os.path.basename(item))#图像名字
    #img_names输出为图像名字列表，包含后缀
#print(img_names)

for img in tqdm(img_names):
    # 获取图像文件夹下中的每一幅图像（包含路径和后缀）
    img_dir = src_img_dir + img
    im = Image.open(img_dir)
    width, height = im.size
    # open the crospronding txt file
    #splitlines()返回一个包含各行作为元素的列表。
    item = img.split("/")[-1]
    temp1, temp2 = os.path.splitext(item)
    txt_dir = src_txt_dir + '/' + temp1 + '.txt'
    gt = open(txt_dir).read().splitlines()#将txt中的每一行作为列表的元素，输出全部内容
    # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    #open()中的参数“w”打开一个文件只用于写入。
    # 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
    # 如果该文件不存在，创建新文件。
    xml_save = src_xml_dir + '/' + img[:-4] + '.xml'
    for img_each_label in gt:#gt 包含txt全部内容，以每行内容为一个元素的列表
        #以空格为分割符的方式提取 gt=['ship1 539 355 563 391','ship2 397 25 416 48']
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        #print(spt) #spt 读取txt中的第一行内容，spt=['ship1','539','355','563','391']
        # spt打印['Images/s1.jpg', '391', '243', '428', '355', '426', '249', '468', '367', '']
        
        pascal_writer = Writer(img_dir, width, height)
        pascal_writer.addObject('jyz', spt[1], spt[2],spt[3], spt[4])
        pascal_writer.save(xml_save)