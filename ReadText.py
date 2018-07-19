from numpy import *

'''
def read(filename):
	st = open(filename)
	arrayOLines = st.readlines()
	for line in arrayOLines:
		stList = line.split(' ')
		print(stList)

read('word.txt')

returnMat = zeros((3,3))  # 根据行数创建以0填充的矩阵
listFromLine = [1,2,3,4]
returnMat[1,:] = listFromLine[1:4]
print(returnMat[1,:])
print('---------')
print(returnMat)

import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(224)
for x in range(0,1000,5):
	ax.scatter(x/100,sin(x/100),100,'r')

plt.show()
'''
'''
print(input())
print("----")
print(input())
print("----")
'''

import numpy as np  
import math  
import matplotlib.pyplot as plt  
x=np.arange(0.05,1,0.01)  
y1=[math.log(a,1.5)for a in x]  
y2=[-math.log(a,2)for a in x]  
y3=[math.log(a,3)for a in x]  
plot1=plt.plot(x,y1,'-g',label="log1.5(x)")  
plot2=plt.plot(x,y2,'-r',label="-log2(x)")  
plot3=plt.plot(x,y3,'-b',label="log3(x)")  
plt.legend(loc='lower right')  
plt.show()  