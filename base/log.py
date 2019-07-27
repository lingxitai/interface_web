import logging
# log=logging.getLogger('root')
# log.setLevel(logging.DEBUG)
#
# fh=logging.FileHandler('SystemOut.log')
# sc=logging.StreamHandler()
#
# style=logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
# fh.setFormatter(style)
# sc.setFormatter(style)
#
# log.addHandler(fh)
# log.addHandler(sc)
#
# log.info('123')
from operationConfig import CONFIG
import os


class Log():
    def __init__(self, servername='root'):#默认输出模块名称是root,各模块根据需要输入自己的名称
        self.log1 = logging.getLogger(servername)
        self.log1.setLevel(logging.DEBUG)
        Config = CONFIG()
        logadress = os.path.join(Config.get_config_value('REPORT', 'path'), 'SystemOut.log')
        '''
        读取config.ini中的report-path，通过Run.py文件写入path，每天更新一个路径
        '''
        filelog = logging.FileHandler(logadress)
        screenlog = logging.StreamHandler()
        style = logging.Formatter('%(asctime)s--%(name)s----%(levelname)s--%(message)s')

        filelog.setFormatter(style)
        screenlog.setFormatter(style)
        self.log1.addHandler(filelog)
        self.log1.addHandler(screenlog)

    def log(self):
        return self.log1


if __name__ == '__main__':
    Getlog = Log('123')
    getlog = Getlog.log()
    getlog.info('132')
