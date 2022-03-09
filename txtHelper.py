'''
Author: Uercal
Date: 2021-06-23 16:17:36
LastEditTime: 2021-06-23 16:17:36
Description: file content
'''


# 多path txt交集
from fileinput import filename
import json
from itertools import combinations
from collections import Counter

import functools
import datetime
from ntpath import join
from operator import setitem
from os import fdopen
import os
from pickle import TRUE
import random
from turtle import right

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
                str(len(resultSet))+'数位'+bonusStr+'_t_'+timeStr+'.txt', 'w')
    file.write(','.join(list(resultSet)))
    file.flush()
    file.close()
    pass



# 找空集  
def findEmptySet(txtPath, filePath,handleNumber=3,returnData=False):         
    f = open(txtPath,'r')
    fileName = os.path.basename(txtPath)
    fileName,fileExt = fileName.split('.')    
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
    # returnData
    if returnData == True:
        return resultList
    file = open(filePath+'\\'+ fileName + '_'+str(handleNumber)+'个数据交空处理.txt', 'w')
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

    file = open(filePath+'\\'+fileName+ str(handleNumber)+'_交空频次.txt', 'w')
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
    file = open(filePath+'\\'+'单数频次_' +
                str(len(counterList))+'_t_'+timeStr+'.txt', 'w')
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



def expectNum(a):
    allSet = set(range(0,10))
    l = allSet - set([a])  
    allPickList = list(combinations(l, 2))
    return allPickList    




# if __name__ == '__main__':    
    
#     totalSet = set()
#     for i in range(0,10):
#         pickList = expectNum(i)
#         # iiab
#         for j in range(0,len(pickList)):
#             num1 = pickList[j][0]
#             num2 = pickList[j][1]
#             totalSet.add(str(i)+str(i)+str(num1)+str(num2))
#             totalSet.add(str(i)+str(i)+str(num2)+str(num1))
#         # abii
#             totalSet.add(str(num1)+str(num2)+str(i)+str(i))
#             totalSet.add(str(num2)+str(num1)+str(i)+str(i))
#         # iabi
#             totalSet.add(str(i)+str(num1)+str(num2)+str(i))
#             totalSet.add(str(i)+str(num2)+str(num1)+str(i))
#         # aiib
#             totalSet.add(str(num1)+str(i)+str(i)+str(num2))
#             totalSet.add(str(num2)+str(i)+str(i)+str(num1))
#         # iaib
#             totalSet.add(str(i)+str(num1)+str(i)+str(num2))
#             totalSet.add(str(i)+str(num2)+str(i)+str(num1))
#         # aibi
#             totalSet.add(str(num1)+str(i)+str(num2)+str(i))
#             totalSet.add(str(num2)+str(i)+str(num1)+str(i))            
#         pass
#     l = list(totalSet)
#     l.sort()
#     file = open('E:\\双数_'+str(len(totalSet))+'.txt', 'w')
#     file.write(','.join(l))
#     file.flush()
#     file.close()



def positionTxtCountHandler(txtPath,filePath):
    f = open(txtPath,'r')
    fList = f.read().split(',')    
    fDict = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[]}
    for i in range(0,len(fList)):    
        if '\n' in fList[i]:
            fList[i] = fList[i].replace('\n','')

        length = len(fList[i])        
        fDict[str(length)].append(fList[i])
        
    result = []
    for j in fDict:
        if len(fDict[j]) != 0:
            result.append('['+j+']'+','.join(fDict[j]))
    

    file = open(filePath+'\\'+'数位排序_' +
                '.txt', 'w')
    file.write('\n'.join(result))
    file.flush()
    file.close()        



# 位数限制 交集
def positionNumberInterset(targetList:list[str],filePath:str,positionSet:set,actionType:bool,positionType:bool):    
    positionStr = '单重' if positionType == True else '双重'
    for i in range(0,len(targetList)):
        resultList = []
        if actionType == True:
            # txt
            itemStr = targetList[i]
            for item in positionSet:
                if item[0] in itemStr and item[1] in itemStr and item[2] in itemStr and item[3] in itemStr:
                    resultList.append(item)
            file = open(filePath+'\\'+'位数限制计算'+positionStr+'_'+'第'+str(i+1)+'个结果_'+str(len(resultList))+'.txt','w')
            file.write(','.join(resultList))
            file.flush()
            file.close()
            pass
        else:
            # shoudongrushu
            itemList = list(targetList[i].split(','))
            for item in positionSet:
                if item[0] in itemList[0] and item[1] in itemList[1] and item[2] in itemList[2] and item[3] in itemList[3]:
                    resultList.append(item)
            file = open(filePath+'\\'+'位数限制计算'+positionStr+'_'+'结果_'+str(len(resultList))+'.txt','w')
            file.write(','.join(resultList))
            file.flush()
            file.close()

    os.startfile(filePath)
    pass


# 序号文件 进行分组交并
def orderFileInterBind(cur,filePath,handleNumber,actionType):
    for curPath in cur:
        orderFileHandler(curPath,filePath,handleNumber,actionType)
        pass
    pass

# 序号文件 单文件处理
def orderFileHandler(file,filePath,handleNumber,actionType,returnData=False):
    fileName = os.path.basename(file)
    fileName,fileExt = fileName.split('.')
    # 
    f = open(file,'r')
    if actionType == False:
        _fList = f.read().split('\n')
        fList = [c.split('（')[0] for c in _fList]        
    else:
        fList = f.read().split(',')        
    # 3个为1组 随机多组  
    group = list(combinations(fList, 3))
    interList = random.sample(group,handleNumber)        
    # result 
    result = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    # 每组 平均3个顺序 求交集 得到交集 求并
    for i in range(0,len(interList),4):
        _list = interList[i:i+4]
        bindList = listForInterBind(_list)                
        for j in bindList:
            result[j] = result[j] + 1
        pass        
     
    counterRate = Counter(result).most_common()
    counterList = []
    _counterData = []
    for k in range(0,len(counterRate)):
        numStr = str(counterRate[k][0])
        countStr = str(counterRate[k][1])        
        counterList.append(numStr+'（'+countStr+'）')    
        _counterData.append(numStr)
    if returnData == True:
        return _counterData
    file = open(filePath+'\\'+fileName+'_交空结果交并单数频次_.txt', 'w')
    file.write('\n'.join(counterList))
    file.flush()
    file.close()
    pass

# list 集合 进行求交集
def listForInterBind(list):
    bindSet = set()
    for item in list:
        resultSet = set()
        for i in range(0, len(item)):
            if i == 0:
                resultSet = set(item[i])
            else:
                resultSet = resultSet & set(item[i])            
        bindSet = bindSet | resultSet    
    return bindSet




# fiveEmptyBindInterHandler
def fiveEmptyBindInterHandler(cur,rightNumber):
    for curPath in cur:
        [namePath,checkNumber,boolean] = fiveEmptyBindInterHandlerSingle(curPath,rightNumber)
    pass

# fiveEmptyBindInterHandlerSingle
def fiveEmptyBindInterHandlerSingle(curPath,rightNumber,handleCount):
    # 交空 60 120 180 240 300 360
    numList = [60,120,180]
    _numList = [240,300,360]
    interFinal = []
    for i in range(0,int(handleCount)):
        interPartI = []
        interPartII = []
        interPartIII = []
        interPartIV = []
        bindListI = []
        bindListII = []
        for num in numList:
            resultList = orderFileHandler(curPath,'',num,True,True)        
            lengthRe = len(resultList)
            interPartI.append(resultList[0:5])
            interPartII.append(resultList[lengthRe-5:lengthRe])                 
        for _num in _numList:
            _resultList = orderFileHandler(curPath,'',_num,True,True)
            _lengthRe = len(_resultList)
            interPartIII.append(_resultList[0:5])
            interPartIV.append(_resultList[_lengthRe-5:_lengthRe])
        # 
        bindListI.append(listForInter(interPartI))
        bindListI.append(listForInter(interPartII))
        bindListII.append(listForInter(interPartIII))
        bindListII.append(listForInter(interPartIV))
        # 
        resultBindI = listForBind(bindListI)
        resultBindII = listForBind(bindListII)   
        interFinal.append(resultBindI)
        interFinal.append(resultBindII)
    # 
    # 求总交集
    resultSet = sorted(listForInter(interFinal))    
    # 
    fileName = os.path.basename(curPath)
    fileName,fileExt = fileName.split('.')
    # name
    nameList = ['头','千','百','十']
    namePath = fileName[len(fileName)-1]
    for index in range(0,4):
        if namePath == nameList[index]:
            checkNumber = rightNumber[index]            
    
    boolean = checkNumber in resultSet
    count = 10-len(resultSet)
    return [namePath,resultSet,boolean,count]    


# list for bind
def listForBind(listData):
    resultSet = set()
    for item in listData:
        if len(resultSet)==0:
            resultSet = item
        else:
            resultSet = resultSet | item
    return resultSet    

# list for inter [['3', '1', '5', '2', '0'], ['3', '1', '7', '0', '4'], ['3', '5', '1', '9', '0']] 返回交集
def listForInter(listData):
    resultSet = set()
    for item in listData:                
        setItem = set(item)
        if len(resultSet) == 0:
            resultSet = setItem
        else:
            resultSet = resultSet & setItem
    return resultSet



def testDemo(filePath):
    wanIndex = [6,9,4,1,3,7,8,0,2,5]
    wan = [1840,1835,1826,1807,1806,1803,1791,1779,1774,1739]
    # 
    qianIndex = [4,1,2,0,8,9,7,5,6,3]
    qian = [1836,1833,1824,1801,1801,1800,1798,1786,1762,1759]
    # 
    baiIndex = [7,0,5,6,4,9,1,3,2,8]
    bai = [1832,1831,1823,1821,1795,1791,1787,1787,1773,1760]
    # 
    shiIndex = [6,0,8,5,1,7,4,3,2,9]
    shi = [1839,1827,1821,1810,1805,1801,1791,1789,1778,1739]

    result = {}
    for w in range(0,10):
        for q in range(0,10):
            for b in range(0,10):
                for s in range(0,10):
                    number = str(wanIndex[w])+str(qianIndex[q])+str(baiIndex[b])+str(shiIndex[s])
                    people = wan[w]*qian[q]*bai[b]*shi[s]/3000/3000/3000
                    if people>=380 and people<=400:
                        result[number] = people
    result = sorted(result.items(), key = lambda kv:(kv[1], kv[0]))
    count = len(result)
    listData = []
    for item in result:
        listData.append(item[0]+' : '+str(item[1]))

    file = open(filePath+'\\'+ '380到400_'+ str(count) +'_.txt', 'w')
    file.write('\n'.join(listData))
    file.flush()
    file.close()