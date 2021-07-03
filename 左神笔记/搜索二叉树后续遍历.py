#字节面试题
# 已知一个搜索二叉树后序遍历的数组posArr
# 请根据posArr，重建出整个树
# 返回新建树的头节点
#
#
posArr = [2, 4, 3, 6, 8, 7, 5]

if __name__ == "__main__":
    leftTree = []
    rightTree = []
    rootNode = posArr[-1]  #获取根节点
    for i in posArr:
        if i < rootNode:
            leftTree.append(i)
        elif i != rootNode:
            rightTree.append(i)
    +-
