# -*- coding:utf-8 -*-
# function     测试不同bitrate下，自适应表格估算FPS和Res的效果
# create time  2017/07/19
# creator      崔鑫鑫

import os
import re
import time
from subprocess import Popen, PIPE
import numpy as np
from numpy import *

from function.logger import logger

if __name__ == '__main__':
    print('Start!')
    logger('1', '1')
