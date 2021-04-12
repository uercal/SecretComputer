# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_config(object):
    def setupUi(self, config):
        config.setObjectName("config")
        config.resize(587, 586)
        self.layoutWidget = QtWidgets.QWidget(config)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addSection = QtWidgets.QPushButton(self.layoutWidget)
        self.addSection.setObjectName("addSection")
        self.gridLayout.addWidget(self.addSection, 9, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        self.gridLayout.addWidget(self.tableWidget, 7, 0, 1, 5)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)
        self.leftSection = QtWidgets.QLineEdit(self.layoutWidget)
        self.leftSection.setObjectName("leftSection")
        self.gridLayout.addWidget(self.leftSection, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 2, 1, 1)
        self.excelSection = QtWidgets.QLineEdit(self.layoutWidget)
        self.excelSection.setObjectName("excelSection")
        self.gridLayout.addWidget(self.excelSection, 2, 3, 1, 2)
        self.isRange = QtWidgets.QCheckBox(self.layoutWidget)
        self.isRange.setObjectName("isRange")
        self.gridLayout.addWidget(self.isRange, 6, 1, 1, 1)
        self.sourceCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.sourceCount.setObjectName("sourceCount")
        self.gridLayout.addWidget(self.sourceCount, 1, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.miniSection = QtWidgets.QLineEdit(self.layoutWidget)
        self.miniSection.setObjectName("miniSection")
        self.gridLayout.addWidget(self.miniSection, 5, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.excelCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.excelCount.setObjectName("excelCount")
        self.gridLayout.addWidget(self.excelCount, 3, 3, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 12, 0, 1, 1)
        self.handlerCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.handlerCount.setText("")
        self.handlerCount.setObjectName("handlerCount")
        self.gridLayout.addWidget(self.handlerCount, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lineTxtRandomGroup = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineTxtRandomGroup.setObjectName("lineTxtRandomGroup")
        self.gridLayout.addWidget(self.lineTxtRandomGroup, 11, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.insideCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.insideCount.setObjectName("insideCount")
        self.gridLayout.addWidget(self.insideCount, 5, 1, 1, 1)
        self.isSingle = QtWidgets.QCheckBox(self.layoutWidget)
        self.isSingle.setObjectName("isSingle")
        self.gridLayout.addWidget(self.isSingle, 6, 0, 1, 1)
        self.rightSection = QtWidgets.QLineEdit(self.layoutWidget)
        self.rightSection.setObjectName("rightSection")
        self.gridLayout.addWidget(self.rightSection, 4, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.miniCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.miniCount.setObjectName("miniCount")
        self.gridLayout.addWidget(self.miniCount, 6, 3, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.rightNumber = QtWidgets.QLineEdit(self.layoutWidget)
        self.rightNumber.setObjectName("rightNumber")
        self.gridLayout.addWidget(self.rightNumber, 0, 1, 1, 1)
        self.lineTxtRandom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineTxtRandom.setObjectName("lineTxtRandom")
        self.gridLayout.addWidget(self.lineTxtRandom, 9, 1, 1, 1)
        self.delSection = QtWidgets.QPushButton(self.layoutWidget)
        self.delSection.setObjectName("delSection")
        self.gridLayout.addWidget(self.delSection, 9, 4, 1, 1)
        self.sourceSection = QtWidgets.QLineEdit(self.layoutWidget)
        self.sourceSection.setObjectName("sourceSection")
        self.gridLayout.addWidget(self.sourceSection, 0, 3, 1, 1)
        self.totalCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.totalCount.setObjectName("totalCount")
        self.gridLayout.addWidget(self.totalCount, 1, 1, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 2, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(133)
        self.gridLayout.addWidget(self.tableWidget_2, 8, 0, 1, 5)
        self.fiftyCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.fiftyCount.setObjectName("fiftyCount")
        self.gridLayout.addWidget(self.fiftyCount, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.lineTxtRandomCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineTxtRandomCount.setObjectName("lineTxtRandomCount")
        self.gridLayout.addWidget(self.lineTxtRandomCount, 12, 1, 1, 1)
        self.hundredCount = QtWidgets.QLineEdit(self.layoutWidget)
        self.hundredCount.setObjectName("hundredCount")
        self.gridLayout.addWidget(self.hundredCount, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.buttonOk = QtWidgets.QDialogButtonBox(config)
        self.buttonOk.setGeometry(QtCore.QRect(190, 520, 179, 23))
        self.buttonOk.setOrientation(QtCore.Qt.Horizontal)
        self.buttonOk.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonOk.setObjectName("buttonOk")

        self.retranslateUi(config)
        self.buttonOk.accepted.connect(config.accept)
        self.buttonOk.rejected.connect(config.reject)
        self.isRange.toggled['bool'].connect(self.tableWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(config)
        config.setTabOrder(self.rightNumber, self.totalCount)
        config.setTabOrder(self.totalCount, self.hundredCount)
        config.setTabOrder(self.hundredCount, self.fiftyCount)
        config.setTabOrder(self.fiftyCount, self.handlerCount)
        config.setTabOrder(self.handlerCount, self.insideCount)
        config.setTabOrder(self.insideCount, self.tableWidget)

    def retranslateUi(self, config):
        _translate = QtCore.QCoreApplication.translate
        config.setWindowTitle(_translate("config", "配置信息"))
        self.addSection.setText(_translate("config", "增加区间"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("config", "范围"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("config", "千位"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("config", "百位"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("config", "十位"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("config", "个位"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("config", "123"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("config", "12314543"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("config", "345345"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("config", "345345345"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("config", "自定义人数"))
        self.label.setText(_translate("config", "落入号码"))
        self.label_9.setText(_translate("config", "自定义单区间"))
        self.isRange.setText(_translate("config", "开启位数限制"))
        self.label_6.setText(_translate("config", "每次结果交集次数"))
        self.label_2.setText(_translate("config", "总数据人数"))
        self.label_16.setText(_translate("config", "txt随机计算次数"))
        self.label_15.setText(_translate("config", "txt随机每组数量"))
        self.label_12.setText(_translate("config", "批量excel区间"))
        self.label_17.setText(_translate("config", "txt随机组数"))
        self.label_4.setText(_translate("config", "100人组数"))
        self.label_7.setText(_translate("config", "概率测试总次数"))
        self.label_3.setText(_translate("config", "交叉第一组"))
        self.isSingle.setText(_translate("config", "只计算总人数"))
        self.label_5.setText(_translate("config", "50人组数"))
        self.label_14.setText(_translate("config", "批量两头区间"))
        self.label_8.setText(_translate("config", "填入ABCD范围"))
        self.delSection.setText(_translate("config", "减少区间"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("config", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("config", "总人数区间"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("config", "100人区间"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("config", "50人区间"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("config", "交叉人数"))
        self.label_13.setText(_translate("config", "批量excel人数"))
