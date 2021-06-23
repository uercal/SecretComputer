'''
Author: Uercal
Date: 2021-06-15 14:39:35
LastEditTime: 2021-06-15 14:49:37
Description:  Excel处理方法类
'''
import os
import helper
#
import win32com.client as win32
import xlwt
import json

# 根据给定索引集 进行websheet读取写入numbers


def readWbFromIndex(ws, indexes, table_name, set_range):
    #
    global configuration
    with open("setting.json", "r") as f:
        setting = f.read()
    configuration = json.loads(setting)
    isRange = configuration['isRange']
    #
    numbers = helper.init4Numbers()
    for _i in range(0, len(indexes)):
        rx = indexes[_i] + 1
        w1 = str(ws.cell(row=rx, column=1).value)
        # 千
        w2 = str(ws.cell(row=rx, column=2).value)
        # 百
        w3 = str(ws.cell(row=rx, column=3).value)
        # 十
        w4 = str(ws.cell(row=rx, column=4).value)
        # 个
        w5 = str(ws.cell(row=rx, column=5).value)
        if w2 == "None":
            break
        #
        if isRange == 1:
            _qianRange = list(map(int, configuration['qianRange']))
            _baiRange = list(map(int, configuration['baiRange']))
            _shiRange = list(map(int, configuration['shiRange']))
            _geRange = list(map(int, configuration['geRange']))
            for i in range(0, len(w2)):
                if _qianRange.count(int(w2[i])) <= 0:
                    continue
                for j in range(0, len(w3)):
                    if _baiRange.count(int(w3[j])) <= 0:
                        continue
                    for m in range(0, len(w4)):
                        if _shiRange.count(int(w4[m])) <= 0:
                            continue
                        for n in range(0, len(w5)):
                            if _geRange.count(int(w5[n])) <= 0:
                                continue
                            numbers[w2[i] + w3[j] + w4[m] +
                                    w5[n]].append(w1)
            pass
        else:
            for i in range(0, len(w2)):

                for j in range(0, len(w3)):

                    for m in range(0, len(w4)):

                        for n in range(0, len(w5)):

                            index = str(w2[i])+str(w3[j]) + \
                                str(w4[m])+str(w5[n])
                            numbers[index].append(w1)

            pass
    #
    for i in range(0, 10000):
        n = "%04d" % i
        numbers[n].sort()
    #
    numbers = numbers.items()
    result = sorted(numbers, key=lambda i: len(i[1]), reverse=True)
    #
    targetSet = set()
    for item in result:
        memberCount = len(item[1])
        if memberCount >= set_range[0] and memberCount <= set_range[1]:
            targetSet.add(item[0])
            pass
    return targetSet


def readWbFromIndexSource(ws, indexes, filePath, parentIndex):
    columnList = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
    parts = [
        dict(onePart=('A', 'B'), twoPart=('C', 'D')),
        dict(onePart=('A', 'C'), twoPart=('B', 'D')),
        dict(onePart=('A', 'D'), twoPart=('B', 'C')),
    ]
    #
    key = 1
    for part in parts:
        result = []
        onePart = part['onePart']
        twoPart = part['twoPart']

        for i in range(0, len(indexes)):
            dataList = {'A': '', 'B': '', 'C': '', 'D': ''}
            rx = indexes[i] + 1
            for item in onePart:
                column = columnList[item]
                dataList[item] = (
                    str(ws.cell(row=rx, column=column).value))

            _dataList = dataList.copy()

            for j in range(0, len(indexes)):
                _rx = indexes[j]+1
                for item in twoPart:
                    _column = columnList[item]
                    _dataList[item] = (
                        str(ws.cell(row=_rx, column=_column).value))
                result.append(_dataList)
                _dataList = dataList.copy()

        fullPath = exportSet(filePath, result, 'jiaocha',
                             str(parentIndex)+str(key))
        key += 1
        #
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(fullPath)

        # FileFormat = 51 is for .xlsx extension
        wb.SaveAs(fullPath+"x", FileFormat=51)
        wb.Close()  # FileFormat = 56 is for .xls extension
        excel.Application.Quit()
        #
        os.remove(fullPath)


def exportSet(path, data, bonus='', key=0):
    _workbook = xlwt.Workbook(encoding='utf-8')
    # 样式
    style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style.alignment = al
    # 注意: 在add_sheet时, 置参数cell_overwrite_ok=True, 可以覆盖原单元格中数据。
    # cell_overwrite_ok默认为False, 覆盖的话, 会抛出异常.
    sheet = _workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
    # 获取并写入数据段信息
    sheet.write(0, 0, '姓名', style)
    sheet.write(0, 1, '数据1', style)
    sheet.write(0, 2, '数据2', style)
    sheet.write(0, 3, '数据3', style)
    sheet.write(0, 4, '数据4', style)
    for row in range(0, len(data)):
        for index in range(0, 4):
            sheet.write(row+1, 0, 'A'+str(row+1), style)
            sheet.write(row+1, index+1, int(data[row]
                                            [['A', 'B', 'C', 'D'][index]]), style)
    #
    if bonus == '':
        fullPath = path+'\\源文件'+'总计'+str(len(data))+'.xls'
    if bonus == 'add':
        fullPath = path+'\\叠加文件'+str(key)+'.xls'
    if bonus == 'leijia':
        fullPath = path+'\\指定数量累加文件'+str(key)+'.xls'
    if bonus == 'jiaocha':
        fullPath = path+'\\交叉文件'+str(key)+'.xls'
    if bonus == 'zuhe':
        fullPath = path+'\\组合文件'+str(key)+'.xls'
    _workbook.save(fullPath)
    return fullPath


# 单纯累加
def readWbFromIndexAdd(wsList, eachFileDataCount, filePath, parentIndex):
    indexes = list(range(1, eachFileDataCount + 1))
    columnList = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
    parts = ('A', 'B', 'C', 'D')
    #
    result = []
    for ws in wsList:
        #
        for j in range(0, len(indexes)):
            dataList = {'A': '', 'B': '', 'C': '', 'D': ''}
            for item in parts:
                _column = columnList[item]
                _rx = indexes[j]+1
                dataList[item] = (
                    str(ws.cell(row=_rx, column=_column).value))
            result.append(dataList)
        #
    fullPath = exportSet(filePath, result, 'leijia',
                         str(parentIndex))
    #
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fullPath)

    # FileFormat = 51 is for .xlsx extension
    wb.SaveAs(fullPath+"x", FileFormat=51)
    wb.Close()  # FileFormat = 56 is for .xls extension
    excel.Application.Quit()
    #
    os.remove(fullPath)

# 交叉累加


def readWbFromIndexAddSource(ws, _ws, sourceCount, filePath, parentIndex):
    indexes = list(range(1, sourceCount*2 + 1))
    columnList = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
    parts = [
        dict(onePart=('A', 'B'), twoPart=('C', 'D')),
        dict(onePart=('A', 'C'), twoPart=('B', 'D')),
        dict(onePart=('A', 'D'), twoPart=('B', 'C')),
    ]
    #
    key = 1
    for part in parts:
        result = []
        onePart = part['onePart']
        twoPart = part['twoPart']
        #
        for i in range(0, len(indexes)):
            dataList = {'A': '', 'B': '', 'C': '', 'D': ''}
            for item in onePart:
                column = columnList[item]
                if i >= sourceCount:
                    rx = indexes[i-sourceCount] + 1
                    dataList[item] = (
                        str(_ws.cell(row=rx, column=column).value))
                else:
                    rx = indexes[i] + 1
                    dataList[item] = (
                        str(ws.cell(row=rx, column=column).value))

            _dataList = dataList.copy()

            for j in range(0, len(indexes)):
                for item in twoPart:
                    _column = columnList[item]
                    if j >= sourceCount:
                        _rx = indexes[j-sourceCount]+1
                        _dataList[item] = (
                            str(_ws.cell(row=_rx, column=_column).value))
                    else:
                        _rx = indexes[j]+1
                        _dataList[item] = (
                            str(ws.cell(row=_rx, column=_column).value))
                result.append(_dataList)
                _dataList = dataList.copy()

        #
        fullPath = exportSet(filePath, result, 'add',
                             str(parentIndex)+str(key))
        key += 1
        #
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(fullPath)

        # FileFormat = 51 is for .xlsx extension
        wb.SaveAs(fullPath+"x", FileFormat=51)
        wb.Close()  # FileFormat = 56 is for .xls extension
        excel.Application.Quit()
        #
        os.remove(fullPath)
