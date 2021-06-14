
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
    for i in range(0,100000):
        n = "%05d" % i
        tartget.add(n)
    return tartget