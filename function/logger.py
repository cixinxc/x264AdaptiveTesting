# -*- coding:utf-8 -*-
import time
import os


def logger(logFileName, logInfo):
    # 当前文件的路径
    currentPath = os.getcwd()
    # 当前文件的父路径
    # fatherPath = os.path.abspath(os.path.dirname(currentPath) + os.path.sep + ".")
    logFilePath = '%s\\log\\' % currentPath
    logFile = open(r'%s%s.txt' % (logFilePath, logFileName), 'a+')
    print('%s\t\t%s' % (logInfo, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))), logFile)
    logFile.flush()
    logFile.close()
