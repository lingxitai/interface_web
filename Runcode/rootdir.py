'''
将当前项目文件添加到环境变量
'''
import os
import sys

sys.path.insert(0,(os.path.dirname(os.path.split(os.path.abspath(__file__))[0])))