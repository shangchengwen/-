from math import log
import operator

# 计算给定数据集的香农熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts={}    # 类别字典 key类别名称 value该类别数量
	# 遍历所有的数据
	for featVec in dataSet:
		currentLabel = featVec[-1]  # 数据的最后一项内容
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel]+=1
	shannonEnt= 0.0
	# 遍历类别字典
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries   # prob = 该类别的数量/数据的总数
		#print(prob * log(prob,2));
		shannonEnt -= prob * log(prob,2)
	return shannonEnt

def createDataSet():
	dataSet = [[1,1,'yes'],
	[1,1,'yes'],
	[1,0,'no'],
	[0,1,'no'],
	[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels

# 按照给定特征划分数据集
# 三个输入参数：待划分的数据集 划分数据集的特征 需要返回的特征的值
# 数据集，第几列，值为value，  的数据集
def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0])-1        # 每条数据有多少特征 每条数据的最后一个当作类别
	baseEntropy = calcShannonEnt(dataSet)  # 返回该数据集的香农熵
	bestInfoGain = 0.0
	bestFeature = -1       # 最好的
	# 分析每一个特征
	for i in range(numFeatures):
		# 列表生成式。[i for i in range(10)],会生成一个[0,1,2,3,4,5,6,7,8,9]的列表
		# 生成对应列特征的的列表
		featList = [example[i] for example in dataSet]
		# 只留下不重复的元素集合
		uniqueVals = set(featList)

		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)   # 对应列特定值的数据集
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)

		# print("-------------")
		# print(baseEntropy)      # 总数据的香农熵
		# print(newEntropy)       # 对应特定值的数据集的香农熵的和 
		
		infoGain = baseEntropy - newEntropy
		
		# print(infoGain)       # 香农熵的差值
		# print(bestInfoGain)   # 差越大 说明该特征越适合作为划分 依据

		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
			# print("赋值")
		# print("-------------")
	return bestFeature

# 返回出现次数做多的分类名称
def majorityCnt(ClassList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),
		key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]  # 所有类别的数组
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(ClassList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree