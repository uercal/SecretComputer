'''
Author: Uercal
Date: 2021-06-23 16:17:36
LastEditTime: 2021-06-23 16:17:36
Description: file content
'''


# 多path txt交集
import json


def mutilTxtCheck(txtPathList, filePath, fileLabel, rightNumber=0, isRange=0):
    resultSet = set()
    bonusStr = ''
    for path in txtPathList:
        f = open(path, "r")  # 设置文件对象
        tSet = set(f.read().split(','))
        if len(resultSet) == 0:
            resultSet = tSet
            pass
        else:
            resultSet = resultSet.intersection(tSet)
        pass
     # 位数筛选 开启判定
    if isRange == 1:
        resultSet = positionRangeFilter(resultSet)
    # 判断命中
    if rightNumber != 0:
        if len({rightNumber} & resultSet) > 0:
            bonusStr = '_命中'
    file = open(filePath+'\\'+fileLabel + '_' +
                str(len(resultSet))+bonusStr+'.txt', 'w')
    file.write(','.join(list(resultSet)))
    file.flush()
    file.close()
    pass


# txt 位数筛选
def positionRangeFilter(resultSet: set):
    with open("setting.json", "r") as f:
        setting = f.read()
    configuration = json.loads(setting)
    # range position
    newSet = set()
    qianRange = list(map(int, configuration['qianRange']))
    baiRange = list(map(int, configuration['baiRange']))
    shiRange = list(map(int, configuration['shiRange']))
    geRange = list(map(int, configuration['geRange']))
    resultList = list(resultSet)
    for i in range(0, len(resultList)):
        if len(str(resultList[i])) == 4:
            if qianRange.count(int(resultList[i][0])) <= 0:
                continue
            if baiRange.count(int(resultList[i][1])) <= 0:
                continue
            if shiRange.count(int(resultList[i][2])) <= 0:
                continue
            if geRange.count(int(resultList[i][3])) <= 0:
                continue
            newSet.add(resultList[i])
    return newSet
