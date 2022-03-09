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
