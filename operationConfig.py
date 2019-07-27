import os
from configparser import ConfigParser

PROJECT_DIR = os.path.split(os.path.abspath(__file__))[0]
CONFIG_PATH =os.path.join(PROJECT_DIR,'config','config.ini')

# config=ConfigParser()
# config.read(CONFIG_PATH,encoding='utf-8')
# cc=config.get('HTTP','scheme')
# print(cc)
# config.set('HTTP','port','8000')
# with open(CONFIG_PATH,'r+',encoding='utf-8') as file:
#     config.write(file)
class CONFIG():
    configfile=ConfigParser()
    configfile.read(CONFIG_PATH,encoding='utf-8')
    def get_config_value(self,section,option):
        '''
        用configfile=ConfigParser()类中的get方法通过section,option获取值
        :param section: config模块名称
        :param option: config元素的键
        :return:
        '''
        value=self.configfile.get(section, option)
        return value
    def set_config_value(self,section,option,value):
        '''
        用于对config.ini设置值，需要存在section,才能添加成功
        :param section:
        :param option:
        :param value: 
        :return:
        '''
        self.configfile.set(section,option,value)
        with open(CONFIG_PATH,'r+',encoding='utf-8') as file:
            self.configfile.write(file)
if __name__=='__main__':
    config=CONFIG()
    vv=config.get_config_value('HTTP','baseurl')
    print(vv)
    config.set_config_value('HTTP','wfw','122')