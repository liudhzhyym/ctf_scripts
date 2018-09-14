#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:	0.01
#Create:	2016-01-30
#Authoruis:	kun/

import array
import sys

from util import traversal_dir
from util import operation

#木马特征
def start(param):
	print "scaninng now....."
	ls = operation.readRetList("dictionaries/rule.txt")#TODO 读取方式升级为用户自定义
	cmp(param, ls)	

#查找木马
def cmp(dir, features):
	suspicious = []
	file_list = traversal_dir.traversal_dir(dir)
	for filepath in file_list:
		if operation.findListStr(filepath, features):#TODO 根据查找到的特征数量定义优先级
			suspicious.append(filepath + "\n")
	operation.writeList("result/result.txt", suspicious,'w')#TODO 写入方式升级为用户自定义
	print "result.txt 已保存到scan/result目录"
		


			

if __name__ == '__main__':
	start(sys.argv[1])
		
