#-*- coding: UTF-8 -*-
import re
import matplotlib.pyplot as plt 
# ��Ҫkali�����������ļ����ݸ�ʽ��(178,114)

f = open(r'1.txt', 'r+')
string = f.read()

# ������ʽ
patternX = '\((\d+),'
patternY = ',(\d+)\)'
 
# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
matchX = re.findall(patternX, string, re.M)
matchY = re.findall(patternY, string, re.M)


#תΪint�б�
matchX = [ int(x) for x in matchX ]
matchY = [ int(y) for y in matchY ]



#plt.plot(matchX,matchY) 
plt.scatter(matchX,matchY) 

plt.show()  