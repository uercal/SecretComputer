'''
Author: Uercal
Date: 2021-06-15 09:39:19
LastEditTime: 2021-06-15 14:42:52
Description: file content
'''

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
