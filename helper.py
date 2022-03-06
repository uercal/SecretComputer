'''
Author: Uercal
Date: 2021-06-15 09:39:19
LastEditTime: 2021-06-15 14:42:52
Description: file content
'''
from fileinput import filename
from math import trunc
import sys
from tkinter.constants import FALSE, NONE
from tokenize import Number
from typing import ItemsView
from PyQt5.QtCore import right
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from tkinter import Tk, filedialog
from easygui import fileopenbox, diropenbox, ccbox, enterbox, passwordbox,multenterbox
import os
from collections import Counter
#
from openpyxl.descriptors.base import Alias
import win32com.client as win32
#
from itertools import combinations, permutations

from txtHelper import listForInter
#
#

def init4NumbersSet():
    target = set()
    for i in range(0, 10000):
        n = "%04d" % i
        target.add(n)
    return target


def init4Numbers():
    # 所有单码集
    numbers = {}
    for i in range(0, 10000):
        n = "%04d" % i
        numbers[n] = []
    return numbers


def init5Numbers():
    # 所有单码集
    numbers = {}
    for i in range(0, 100000):
        n = "%05d" % i
        numbers[n] = []
    return numbers


def init5NumbersSet():
    tartget = set()
    for i in range(0, 100000):
        n = "%05d" % i
        tartget.add(n)
    return tartget


def listForBind(list):
    result = set()
    for item in list:
        result = result | set(item)
    return result



if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    cur = filedialog.askopenfilename(filetypes=[('text files', '.txt')])
    # 结果目录
    filePath = diropenbox('结果存放目录')
    # action handler
    f = open(cur,'r')
    fList = f.read().split('\n')
    valueList = []
    totalList = {}
    indexSet = {}
    for item in fList:
        [index,value] = item.split(':')
        totalList[value] = index
        valueList.append(value)
        indexSet[index] = 0
    # 
    group = list(combinations(valueList, 4))
    result = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    
    resultList = []
    indexStrList = []
    for item in group:
        item = [a for a in item]
        bindItem = listForBind(item)
        bindItem = [int(b) for b in bindItem]
        resultItem = list(set(range(0,10)) - set(bindItem))
        if len(resultItem)>0:
            listResult = [str(c) for c in resultItem]
            for j in listResult:
                result[j] = result[j]+1
            resultStr = ','.join(listResult)
            resultList.append(resultStr)
        if len(resultItem)==0:
            indexStr = ''
            for j in item:
                indexStr = indexStr+totalList[j]
                indexSet[totalList[j]] = indexSet[totalList[j]]+1
            indexStrList.append(indexStr)
    # 
    counterRate = Counter(result).most_common()
    counterList = []
    for k in range(0,len(counterRate)):
        numStr = str(counterRate[k][0])
        countStr = str(counterRate[k][1])        
        counterList.append(numStr+'（'+countStr+'）')    
    # 
    counterIndexRate = Counter(indexSet).most_common()
    counterIndexList = []
    for k in range(0,len(counterIndexRate)):
        _numStr = str(counterIndexRate[k][0])
        _countStr = str(counterIndexRate[k][1])        
        counterIndexList.append(_numStr+'（'+_countStr+'）')   

    __file = open(filePath+'\\'+'满集结果组合.txt', 'w')
    __file.write('\n'.join(indexStrList))
    __file.flush()
    __file.close()
    ___file = open(filePath+'\\'+'满集结果频次.txt', 'w')
    ___file.write('\n'.join(counterIndexList))
    ___file.flush()
    ___file.close()
    # 
    _file = open(filePath+'\\'+'测试差集结果频次.txt', 'w')
    _file.write('\n'.join(counterList))
    _file.flush()
    _file.close()
    # 
    file = open(filePath+'\\'+'测试差集结果.txt', 'w')
    file.write('\n'.join(resultList))
    file.flush()
    file.close()
    os.startfile(filePath)
    root.destroy()
    root.mainloop()


    pass