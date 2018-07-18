from numpy import *
import operator
import numpy as np
np.set_printoptions(threshold=np.inf) # 全部显示

# 创建数据
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

# k-近邻算法(坐标，坐标数组，对应的类型，前k个数据中最多)
def classify0(inX,dataSet,labels,k):
	# print("**classify0**")
	dataSetSize = dataSet.shape[0]    # 数组个数,数据个数
	diffMat = tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat = diffMat**2
	sqDistance = sqDiffMat.sum(axis=1)
	distance = sqDistance**0.5
	# print(distance)
	sortedDistIndicies = distance.argsort()  #返回从小到大的索引值
	# print(sortedDistIndicies)
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]  # 最小的距离的类别标签
		 # classCount.get(voteIlabel,0)返回字典classCount中voteIlabel元素对应的值,
		 # 若不存在voteIlabel，则字典classCount中生成voteIlabel元素，并使其对应的数字为0
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1 

	# print(classCount.items())

	# classCount.items() 获得所有键值对

	# a = [1,2,3] 
	# b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
	# b(a) 
	# 2 
	# b=operator.itemgetter(1,0)   //定义函数b，获取对象的第1个域和第0个的值
 	# b(a) 
    # (2, 1) 

    # reverse=True 降序
	sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

# 将文本转换为Numpy 矩阵
def file2matrix(filename):
	fr = open(filename)      # 打开文件
	arrayOLines = fr.readlines()  # 按行读取 字符串数组
	numberOfLines = len(arrayOLines)   # 文件内容行数
	returnMat = zeros((numberOfLines,3))  # 根据行数创建以0填充的矩阵

	classLabelVector = []
	index = 0

	for line in arrayOLines:
		line = line.strip()     # 移除头尾的字符 空格
		listFromLine = line.split('\t')  # 根据 \t 拆分
		# 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
		# [0:3]从第0个取，取3-0个数据  [1:4]从第0个取，取4-1个数据
		returnMat[index,:] = listFromLine[0:3]
		if listFromLine[-1] == 'didntLike':
			classLabelVector.append(1)
		elif listFromLine[-1] == 'smallDoses':
			classLabelVector.append(2)
		elif listFromLine[-1] == 'largeDoses':
			classLabelVector.append(3)
		index += 1
	return returnMat,classLabelVector

# 归一化特征值 某一数据/(这一列最大值 - 最小值) 百分比0-1之间的数
def autoNorm(dataSet):
	# dataSet.min()) #无参，所有中的最小值
	# dataSet.min(0)) # axis=0; 每列的最小值
	# dataSet.min(1)) # axis=1；每行的最小值
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals # 每一列最大值-最小值

	normDataSet = zeros(shape(dataSet))  # 归零矩阵

	m = dataSet.shape[0]   # 数组个数 m = 1000

	# a=[[1,2,3],[5,4]]
	# tile(a,[2,3])
	# array([[[1, 2, 3], [5, 4], [1, 2, 3], [5, 4], [1, 2, 3], [5, 4]],
	# [[1, 2, 3], [5, 4], [1, 2, 3], [5, 4], [1, 2, 3], [5, 4]]])
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals

def datingClassTest():
	hoRatio = 0.90      # 抽取数量百分比 随机抽取10%
	datingDataMat,datingLabels = file2matrix('datingTestSet.txt') #读取数据
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)  # 测试数据的数量
	errorCount = 0.0   # 错误数据的数量

	for i in range(numTestVecs):
		# normMat[i,:] 取二维数组 第i行的所有的数据
		# normMat[numTestVecs:m,:]  # 去除测试数据剩下的数据 二维数组
		# datingLabels[numTestVecs:m]  # 去除测试数据剩下的数据

		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],
			datingLabels[numTestVecs:m],3)
		print ("the classifier came back with:%d,the real answer is:%d"
		%(classifierResult,datingLabels[i]))
		if(classifierResult!=datingLabels[i]):
			print("-----")
			errorCount += 1.0
	print ("the total error rate is:%f"%(errorCount/float(numTestVecs)))

# 是否是想要相亲的对象
def classifyPerson():
	resultList = ['not at all','in small doses','in large doses']
	percentTats = float(input("percentage of time spent playing video games?"))
	ffMiles = float(input("frequent flier miles earned per year?"))
	iceCream = float(input("liters of ice cream consumed per year?"))
	datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print("You will probably like this person: ",resultList[classifierResult-1])

# 读取图片
def img2Vector(filename):
	# returnVect = zeros((1,1024))
	# print(returnVect)
	returnVect = zeros([1,1024]) # 创建一维数组个数1024
	print(returnVect)
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()  # 读出每一行数据
		print(lineStr)
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect


