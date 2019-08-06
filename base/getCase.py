'''
通过baseDB和operationConfig拼装数据
用于获得案例，以字典的形式，组成列表
'''
from base.baseDB import BaseDB
from operationConfig import CONFIG
from base.log import Log
# basedb=BaseDB()
# data=basedb.get_all_data('select id,casename,frontsql,apipath,requestmethod,requestdata,httpcodecheck from Webserver_testcase')
# print('读取数据库全部内容为{0}'.format(data))
#
# from operationConfig import CONFIG
# config=CONFIG()
# key=config.get_config_value('EXCEL','excel_case_name')
# print('读取ini内容为{0}'.format(eval(key)))
# for i in data:
#     print('读取数据库单条内容为{0}'.format(i))
#     dict1=dict(zip(eval(key),list(i)))
#     print('拼装为字典为{0}'.format(dict1))

class GetCase(object):
    def __init__(self):
        Getlog=Log('getCase')
        self.getlog=Getlog.log()
        self.basedb=BaseDB()
        self.getconfig=CONFIG()

    def get_case_data(self,name=None):
        '''
        获取案例以字典的形式，组成列表，name不输入参数，查询全部数据；输入name对个值以元祖的形式
        ('','')即可查到指定案例数据
        :param name:
        :return:
        '''
        key=eval(self.getconfig.get_config_value('EXCEL','excel_case_name'))
        '''读取的ini文件内容为字符串,通过eval转化为列表为下面zip使用'''
        self.getlog.info('获取字典key值为:{0}'.format(key))
        colsname=self.getconfig.get_config_value('DATABASE','colsname')
        if name:
            sql='select {0} ' \
                'from Webserver_testcase where casename in{1}'.format(colsname,name)
            data=self.basedb.get_all_data(sql)
            list1=[]
            for i in data:
                dict1=dict(zip(key,list(i)))
                self.getlog.info('获取案例拼为字典为: \n {0}'.format(dict1))
                list1.append(dict1)
            self.getlog.info('获取案例将字典加到列表为: \n{0}'.format(list1))
        else:
            sql='select {0} ' \
                'from Webserver_testcase ' .format(colsname)
            data=self.basedb.get_all_data(sql)
            list1=[]
            for i in data:
                dict1=dict(zip(key,list(i)))
                self.getlog.info('获取案例拼为字典为: \n {0}'.format(dict1))
                list1.append(dict1)
            self.getlog.info('获取案例将字典加到列表为: \n{0}'.format(list1))
        return list1

if __name__=='__main__':
    getcase=GetCase()
    # getcase.get_case_data(('获取用户手机号','测试'))
    getcase.get_case_data()


