# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 721, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(650, 470, 75, 23))
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menutxt = QtWidgets.QMenu(self.menu)
        self.menutxt.setObjectName("menutxt")
        self.menuexcel = QtWidgets.QMenu(self.menu)
        self.menuexcel.setObjectName("menuexcel")
        self.menu_5 = QtWidgets.QMenu(self.menuexcel)
        self.menu_5.setObjectName("menu_5")
        self.menupiliangdanqujian = QtWidgets.QMenu(self.menuexcel)
        self.menupiliangdanqujian.setObjectName("menupiliangdanqujian")
        self.menu_6 = QtWidgets.QMenu(self.menuexcel)
        self.menu_6.setObjectName("menu_6")
        self.menu_4 = QtWidgets.QMenu(self.menu)
        self.menu_4.setObjectName("menu_4")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionjiaoji = QtWidgets.QAction(MainWindow)
        self.actionjiaoji.setObjectName("actionjiaoji")
        self.actionchaji = QtWidgets.QAction(MainWindow)
        self.actionchaji.setObjectName("actionchaji")
        self.actionbingji = QtWidgets.QAction(MainWindow)
        self.actionbingji.setObjectName("actionbingji")
        self.actionloadingRecent = QtWidgets.QAction(MainWindow)
        self.actionloadingRecent.setObjectName("actionloadingRecent")
        self.actionexportPast = QtWidgets.QAction(MainWindow)
        self.actionexportPast.setObjectName("actionexportPast")
        self.actionconfig = QtWidgets.QAction(MainWindow)
        self.actionconfig.setObjectName("actionconfig")
        self.actioncheck = QtWidgets.QAction(MainWindow)
        self.actioncheck.setObjectName("actioncheck")
        self.actionmainCheck = QtWidgets.QAction(MainWindow)
        self.actionmainCheck.setObjectName("actionmainCheck")
        self.actionSource = QtWidgets.QAction(MainWindow)
        self.actionSource.setObjectName("actionSource")
        self.actionmini = QtWidgets.QAction(MainWindow)
        self.actionmini.setObjectName("actionmini")
        self.actionAddSource = QtWidgets.QAction(MainWindow)
        self.actionAddSource.setObjectName("actionAddSource")
        self.actionExcelSet = QtWidgets.QAction(MainWindow)
        self.actionExcelSet.setObjectName("actionExcelSet")
        self.actionBind = QtWidgets.QAction(MainWindow)
        self.actionBind.setObjectName("actionBind")
        self.actionactionTwoside = QtWidgets.QAction(MainWindow)
        self.actionactionTwoside.setObjectName("actionactionTwoside")
        self.actiontxtRandom = QtWidgets.QAction(MainWindow)
        self.actiontxtRandom.setObjectName("actiontxtRandom")
        self.actiontxtRandomGroup = QtWidgets.QAction(MainWindow)
        self.actiontxtRandomGroup.setObjectName("actiontxtRandomGroup")
        self.actionmutilCha = QtWidgets.QAction(MainWindow)
        self.actionmutilCha.setObjectName("actionmutilCha")
        self.actionmutilIsRight = QtWidgets.QAction(MainWindow)
        self.actionmutilIsRight.setObjectName("actionmutilIsRight")
        self.actionrandomPickBind = QtWidgets.QAction(MainWindow)
        self.actionrandomPickBind.setObjectName("actionrandomPickBind")
        self.actionrandomGroupBind = QtWidgets.QAction(MainWindow)
        self.actionrandomGroupBind.setObjectName("actionrandomGroupBind")
        self.actiondiyPIckGroupInter = QtWidgets.QAction(MainWindow)
        self.actiondiyPIckGroupInter.setObjectName("actiondiyPIckGroupInter")
        self.actionmutilAdd = QtWidgets.QAction(MainWindow)
        self.actionmutilAdd.setObjectName("actionmutilAdd")
        self.actionStaticsPosition = QtWidgets.QAction(MainWindow)
        self.actionStaticsPosition.setObjectName("actionStaticsPosition")
        self.actionreverseResult = QtWidgets.QAction(MainWindow)
        self.actionreverseResult.setObjectName("actionreverseResult")
        self.actionexcelMissing = QtWidgets.QAction(MainWindow)
        self.actionexcelMissing.setObjectName("actionexcelMissing")
        self.actionsingleOriginPaste = QtWidgets.QAction(MainWindow)
        self.actionsingleOriginPaste.setObjectName("actionsingleOriginPaste")
        self.actionmutilOriginPaste = QtWidgets.QAction(MainWindow)
        self.actionmutilOriginPaste.setObjectName("actionmutilOriginPaste")
        self.actiondirectoryAdd = QtWidgets.QAction(MainWindow)
        self.actiondirectoryAdd.setObjectName("actiondirectoryAdd")
        self.actionpartsSingleExcel = QtWidgets.QAction(MainWindow)
        self.actionpartsSingleExcel.setObjectName("actionpartsSingleExcel")
        self.actionMutilDirAdd = QtWidgets.QAction(MainWindow)
        self.actionMutilDirAdd.setObjectName("actionMutilDirAdd")
        self.actionrandomMutilTxt = QtWidgets.QAction(MainWindow)
        self.actionrandomMutilTxt.setObjectName("actionrandomMutilTxt")
        self.actionmultiPositionHandler = QtWidgets.QAction(MainWindow)
        self.actionmultiPositionHandler.setObjectName("actionmultiPositionHandler")
        self.actionfindEmpty = QtWidgets.QAction(MainWindow)
        self.actionfindEmpty.setObjectName("actionfindEmpty")
        self.actionsingleNumberRate = QtWidgets.QAction(MainWindow)
        self.actionsingleNumberRate.setObjectName("actionsingleNumberRate")
        self.actionpositionCountOrder = QtWidgets.QAction(MainWindow)
        self.actionpositionCountOrder.setObjectName("actionpositionCountOrder")
        self.actiondanshuangPosition = QtWidgets.QAction(MainWindow)
        self.actiondanshuangPosition.setObjectName("actiondanshuangPosition")
        self.actionorderFileCombine = QtWidgets.QAction(MainWindow)
        self.actionorderFileCombine.setObjectName("actionorderFileCombine")
        self.actionfiveEmptyBindInter = QtWidgets.QAction(MainWindow)
        self.actionfiveEmptyBindInter.setObjectName("actionfiveEmptyBindInter")
        self.actionshaCodeFullCha = QtWidgets.QAction(MainWindow)
        self.actionshaCodeFullCha.setObjectName("actionshaCodeFullCha")
        self.menutxt.addAction(self.actionjiaoji)
        self.menutxt.addAction(self.actionchaji)
        self.menutxt.addAction(self.actionbingji)
        self.menutxt.addAction(self.actioncheck)
        self.menutxt.addAction(self.actionBind)
        self.menutxt.addAction(self.actionmutilCha)
        self.menutxt.addAction(self.actionreverseResult)
        self.menutxt.addAction(self.actionmultiPositionHandler)
        self.menutxt.addAction(self.actionfindEmpty)
        self.menutxt.addAction(self.actionsingleNumberRate)
        self.menutxt.addAction(self.actionpositionCountOrder)
        self.menutxt.addAction(self.actiondanshuangPosition)
        self.menutxt.addAction(self.actionorderFileCombine)
        self.menutxt.addAction(self.actionshaCodeFullCha)
        self.menu_5.addAction(self.actionsingleOriginPaste)
        self.menu_5.addAction(self.actionmutilOriginPaste)
        self.menupiliangdanqujian.addAction(self.actionExcelSet)
        self.menupiliangdanqujian.addAction(self.actionpartsSingleExcel)
        self.menu_6.addAction(self.actionAddSource)
        self.menu_6.addAction(self.actionmutilAdd)
        self.menu_6.addAction(self.actionMutilDirAdd)
        self.menuexcel.addAction(self.actionmainCheck)
        self.menuexcel.addAction(self.actionmini)
        self.menuexcel.addAction(self.actionSource)
        self.menuexcel.addAction(self.actionactionTwoside)
        self.menuexcel.addAction(self.menu_5.menuAction())
        self.menuexcel.addAction(self.actionStaticsPosition)
        self.menuexcel.addAction(self.actionexcelMissing)
        self.menuexcel.addAction(self.menupiliangdanqujian.menuAction())
        self.menuexcel.addAction(self.menu_6.menuAction())
        self.menu_4.addAction(self.actiontxtRandom)
        self.menu_4.addAction(self.actiontxtRandomGroup)
        self.menu_4.addAction(self.actionrandomPickBind)
        self.menu_4.addAction(self.actionrandomGroupBind)
        self.menu_4.addAction(self.actiondiyPIckGroupInter)
        self.menu_4.addAction(self.actionrandomMutilTxt)
        self.menu_4.addSeparator()
        self.menu.addAction(self.menutxt.menuAction())
        self.menu.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.menuexcel.menuAction())
        self.menu_2.addAction(self.actionloadingRecent)
        self.menu_2.addAction(self.actionexportPast)
        self.menu_3.addAction(self.actionconfig)
        self.menutest.addAction(self.actionfiveEmptyBindInter)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearButton.setText(_translate("MainWindow", "??????"))
        self.menu.setTitle(_translate("MainWindow", "????????????"))
        self.menutxt.setTitle(_translate("MainWindow", "txt???"))
        self.menuexcel.setTitle(_translate("MainWindow", "excel???"))
        self.menu_5.setTitle(_translate("MainWindow", "????????????????????????"))
        self.menupiliangdanqujian.setTitle(_translate("MainWindow", "???????????????"))
        self.menu_6.setTitle(_translate("MainWindow", "????????????"))
        self.menu_4.setTitle(_translate("MainWindow", "txt?????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.menu_3.setTitle(_translate("MainWindow", "??????"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
        self.actionjiaoji.setText(_translate("MainWindow", "??????"))
        self.actionchaji.setText(_translate("MainWindow", "??????"))
        self.actionbingji.setText(_translate("MainWindow", "??????"))
        self.actionloadingRecent.setText(_translate("MainWindow", "????????????????????????"))
        self.actionexportPast.setText(_translate("MainWindow", "?????????3???????????????"))
        self.actionconfig.setText(_translate("MainWindow", "????????????"))
        self.actioncheck.setText(_translate("MainWindow", "???txt??????"))
        self.actionmainCheck.setText(_translate("MainWindow", "??????????????????"))
        self.actionSource.setText(_translate("MainWindow", "????????????????????????"))
        self.actionmini.setText(_translate("MainWindow", "??????????????????"))
        self.actionAddSource.setText(_translate("MainWindow", "??????????????????"))
        self.actionExcelSet.setText(_translate("MainWindow", "????????????????????????"))
        self.actionBind.setText(_translate("MainWindow", "???txt??????"))
        self.actionactionTwoside.setText(_translate("MainWindow", "?????????????????????"))
        self.actiontxtRandom.setText(_translate("MainWindow", "??????????????????"))
        self.actiontxtRandomGroup.setText(_translate("MainWindow", "??????????????????"))
        self.actionmutilCha.setText(_translate("MainWindow", "???txt????????????"))
        self.actionmutilIsRight.setText(_translate("MainWindow", "??????????????????"))
        self.actionrandomPickBind.setText(_translate("MainWindow", "??????????????????"))
        self.actionrandomGroupBind.setText(_translate("MainWindow", "??????????????????"))
        self.actiondiyPIckGroupInter.setText(_translate("MainWindow", "?????????????????????"))
        self.actionmutilAdd.setText(_translate("MainWindow", "????????????????????????"))
        self.actionStaticsPosition.setText(_translate("MainWindow", "?????????????????????"))
        self.actionreverseResult.setText(_translate("MainWindow", "????????????"))
        self.actionexcelMissing.setText(_translate("MainWindow", "??????????????????"))
        self.actionsingleOriginPaste.setText(_translate("MainWindow", "?????????"))
        self.actionmutilOriginPaste.setText(_translate("MainWindow", "??????"))
        self.actiondirectoryAdd.setText(_translate("MainWindow", "?????????????????????"))
        self.actionpartsSingleExcel.setText(_translate("MainWindow", "?????????????????????"))
        self.actionMutilDirAdd.setText(_translate("MainWindow", "???????????????????????????"))
        self.actionrandomMutilTxt.setText(_translate("MainWindow", "????????????????????????"))
        self.actionmultiPositionHandler.setText(_translate("MainWindow", "????????????????????????"))
        self.actionfindEmpty.setText(_translate("MainWindow", "???????????????"))
        self.actionsingleNumberRate.setText(_translate("MainWindow", "????????????"))
        self.actionpositionCountOrder.setText(_translate("MainWindow", "????????????"))
        self.actiondanshuangPosition.setText(_translate("MainWindow", "?????????????????????"))
        self.actionorderFileCombine.setText(_translate("MainWindow", "??????????????????????????????"))
        self.actionfiveEmptyBindInter.setText(_translate("MainWindow", "????????????????????????"))
        self.actionshaCodeFullCha.setText(_translate("MainWindow", "??????????????????????????????"))
