'''
Author: Uercal
Date: 2021-06-23 16:17:36
LastEditTime: 2021-06-23 16:17:36
Description: file content
'''


# 多path txt交集
import json
from itertools import combinations
from collections import Counter

import functools
import datetime

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




# 单双文件 交并处理
def filesSetHandler(txtPathList, filePath,type='intersect',handleNumber=0):
    if len(txtPathList)>2 or len(txtPathList)==0:
        return False
    resultSet = set()
    if len(txtPathList)==2:
        pass
        f1 = open(txtPathList[0],'r')
        f2 = open(txtPathList[1],'r')
        f1Set = f1.read().split(',')      
        f2Set = f2.read().split(',')
        for i in range(0,len(f1Set)):
            for j in range(0,len(f2Set)):
                if type=='intersect':
                    target = set(f1Set[i]).intersection(set(f2Set[j])) 
                if type=='union':
                    target = set(f1Set[i]).union(set(f2Set[j]))
                if len(target) == 0:
                    continue
                targetList = list(target)                
                targetList.sort()                
                resultSet.add(''.join(targetList))                   
    else:        
        if handleNumber < 2:
            return False        
        f = open(txtPathList[0],'r')
        fSet = f.read().split(',')        
        fList = list(combinations(fSet,handleNumber))        

        for i in range(0,len(fList)):
            itemList = fList[i]
            targetSet = set()
            for j in range(0,handleNumber):
                item = itemList[j]
                if '\n' in item:
                    item = item.replace("\n","")
                if type=='intersect':
                    if j==0:
                        targetSet = set(item)
                    else:
                        targetSet = set(item).intersection(targetSet) 
                if type=='union':                    
                    targetSet = set(item).union(targetSet)
            if len(targetSet)!=0:                                
                targetList = list(targetSet)                
                targetList.sort()                
                resultSet.add(''.join(targetList))                              
     # 位数筛选 开启判定    
    bonusStr = '交集' if type=='intersect' else '并集'
    timeStr = datetime.datetime.now().strftime('%H%M')
    file = open(filePath+'\\'+ str(handleNumber)+'个数据处理_' +
                str(len(resultSet))+'数位'+bonusStr+'_'+timeStr+'.txt', 'w')
    file.write(','.join(list(resultSet)))
    file.flush()
    file.close()
    pass



# 找空集  
def findEmptySet(txtPath, filePath,handleNumber=3):         
    f = open(txtPath,'r')
    fSet = f.read().split(',')
    fList = list(combinations(fSet, handleNumber))    
    resultList = []
    rateList = []
    for i in range(0,len(fList)):
        _itemList = fList[i]
        itemList = []
        for m in range(0,len(_itemList)):
            _item = _itemList[m]
            if '\n' in _item:
                _item = _item.replace("\n","")
            itemList.append(_item)                    

        targetSet = set()
        for j in range(0,handleNumber):
            item = itemList[j]                 
            if j==0:
                targetSet = set(item)
            else:
                targetSet = set(item).intersection(targetSet) 
        
        if len(targetSet)==0:
            targetList = list(itemList)                
            targetList.sort()                
            resultList.append('/'.join(targetList))                              
            for k in range(0,handleNumber):
                rateList.append(itemList[k])
    
    resultList = set(resultList)
    resultList = sorted(resultList,key=functools.cmp_to_key(cmp))
    resultList = list(resultList)
    file = open(filePath+'\\'+ str(handleNumber)+'个数据交空处理_' +
                str(len(resultList))+'.txt', 'w')
    file.write('\n'.join(resultList))
    file.flush()
    file.close()
    # 查找resultList 频次
    counterRate = Counter(rateList).most_common()
    counterList = []
    for k in range(0,len(counterRate)):
        numStr = str(counterRate[k][0])
        countStr = str(counterRate[k][1])
        counterList.append(numStr+'（'+countStr+'）')

    file = open(filePath+'\\'+ str(handleNumber)+'交空频次_' +
                str(len(counterList))+'.txt', 'w')
    file.write('\n'.join(counterList))
    file.flush()
    file.close()
    

    pass



# 数列 单数频次
def singleNumberRate(txtPath,filePath):
    f = open(txtPath,'r')
    fList = f.read().split(',')
    result = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in range(0,len(fList)):
        for m in range(0,len(fList[i])):
            item = str(fList[i][m])                        
            if item =='\n':
                continue
            if '\n' in item:
                item.replace("\n","")            
            result[item] = result[item] + 1
        pass
    counterRate = Counter(result).most_common()
    counterList = []
    for k in range(0,len(counterRate)):
        numStr = str(counterRate[k][0])
        countStr = str(counterRate[k][1])        
        counterList.append(numStr+'（'+countStr+'）')


    timeStr = datetime.datetime.now().strftime('%H%M')
    print(timeStr)
    file = open(filePath+'\\'+'单数频次_' +
                str(len(counterList))+'_'+timeStr+'.txt', 'w')
    file.write('\n'.join(counterList))
    file.flush()
    file.close()
    return counterList    





def cmp(x:str,y:str):
    a= x.split('/')
    b= y.split('/')
    newStrNum1 = a[0] + b[0]
    newStrNum2 = b[0] + a[0]
    if newStrNum2 > newStrNum1:
        return -1
    elif newStrNum2 == newStrNum1:
        _newStrNum1 = a[1] + b[1]
        _newStrNum2 = b[1] + a[1]
        if _newStrNum2 > _newStrNum1:
            return -1
        elif _newStrNum2 == _newStrNum1:                        
            return 0
        else:
            return 1        
    else:
        return 1

