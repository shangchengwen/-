import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

'''
group,labels = kNN.createDataSet()
print(group)
print(labels)

print("-------------")

a = kNN.classify0([0,0],group,labels,3)

print("结果：")
print(a)
'''

'''
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
print(datingDataMat)
print(datingLabels)

fig = plt.figure()
# 图片位置
ax = fig.add_subplot(111)
# scatter(x,y,大小,颜色)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
	20.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
'''

'''
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
normMat,ranges,minVals = kNN.autoNorm(datingDataMat)
# print(normMat)

# kNN.datingClassTest()

kNN.classifyPerson()
'''

'''
testVector = kNN.img2Vector('digits/testDigitsnumFeatures/0_13.txt')
print("--------")
print(testVector[0,0:31])
print(testVector[0,32:63])
'''


import trees
myDat,labels = trees.createDataSet()
print(myDat)
print(labels)

'''
myDat[0][-1] = 'maybe'
value = trees.calcShannonEnt(myDat)
print(value)

a = trees.splitDataSet(myDat,0,1)
print(a)
b = trees.splitDataSet(myDat,0,0)
print(b)
'''

'''
a = trees.chooseBestFeatureToSplit(myDat)
print(a)
'''

myTree = trees.createTree(myDat,labels)
print(myTree)


