# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
decisionNode = dict(boxstyle = "sawtooth",fc = "1") # 边框的样式
leafNode = dict(boxstyle = "round4",fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

# 节点的文字描述,当前位置,开始位置,节点边框的样式
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	# 加标注
	createPlot.ax1.annotate(
		nodeTxt,
		xy = parentPt,
		xycoords = 'axes fraction',
		xytext = centerPt,
		textcoords = 'axes fraction',
		va = "center",
		ha = "center",
		bbox = nodeType,
		arrowprops = arrow_args)

def createPlot():
	plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）   #不显示中文的问题
	fig = plt.figure(1,facecolor = 'white')
	fig.clf()
	# 绘制图
	createPlot.ax1 = plt.subplot(111,frameon = False)
	plotNode(U'决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode(U'叶节点',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()

# 获取叶子节点的数目
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		# 使用Python提供的type()函数可以判断子节点是否为字典类型
		if type(secondDict[key]).__name__ == 'dict':
			numLeafs += getNumLeafs(secondDict)
		else: numLeafs += 1
	return numLeafs

# 获取树的层数
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict)
		else: thisDepth = 1
		if thisDepth > maxDepth:
			maxDepth =  thisDepth
	return maxDepth

createPlot();