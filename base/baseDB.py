import os, sqlite3
from operationConfig import CONFIG
import operationConfig as opconfig
from base.log import Log

getconfig = CONFIG()

Getlog = Log('basedb')
getlog = Getlog.log()
db_path = getconfig.get_config_value('DATABASE', 'db_path')
sqlpath = os.path.join(opconfig.PROJECT_DIR, db_path)
getlog.info('sqllite3的地址为%s' % (sqlpath))


# db=sqlite3.connect(sqlpath)
# cursor=db.cursor()
# data=cursor.execute('select * from Webserver_testcase')
# data1=data.fetchall()
# print(data,data1)
class BaseDB(object):
    def __init__(self):
        try:
            self.db = sqlite3.connect(sqlpath)
            self.cursor = self.db.cursor()
        except ConnectionError as e:
            getlog.error('连接数据报错了，报错信息为：{0}'.format(e))

    def excutesql(self, sql):
        reslut = self.cursor.execute(sql)
        self.db.commit()
        getlog.info('数据库执行结果为{0}'.format(reslut))
        return reslut

    def __close_db(self):
        self.cursor.close()  # 先关cursor再关connect
        self.db.close()
        getlog.info('数据库已关闭')

    def get_all_data(self, sql):
        all_data = self.excutesql(sql)
        data = all_data.fetchall()
        getlog.info('数据库执行get_all_data方法查询结果为: \n {0}'.format(data))
        self.__close_db()
        return data

    def get_one_data(self, sql):
        all_data = self.excutesql(sql)
        data = all_data.fetchone()
        getlog.info('数据库执行get_one_data方法查询结果为: \n {0}'.format(data))
        self.__close_db()
        return data

    def get_row_data(self, sql, rows):  # 查询前几行的数据
        all_data = self.excutesql(sql)
        data = all_data.fetchmany(rows)
        getlog.info('数据库执行get_row_data方法查询结果为: \n {0}'.format(data))
        self.__close_db()
        return data


# from Webserver.models import Testcase
# class DJ_basedb(object):
#     '''
#     此类方法使用objects方法封装，tablename 传入需要查询的表名,
#     方法必须在django框架里应用，不能只run一个文件运行它，即使django是启动的也不行
#     '''
#     def __init__(self,tablename):
#         self.tablename=tablename
#     def getdj_all_data(self):
#         '''
#         此方法为获得全部数据，只是获得QuerySet对象，需要通过迭代for i in 获取内部数据，并通过i.列名获得值
#         :return:
#         '''
#         return eval(self.tablename).objects.all()
#     def getdj_one_date(self,rows):
#         '''
#         此方法用于获得单行数据，rows对应的id号，可直接通过aa=getdj_one_date(1),aa.列名获得值
#         :param rows:
#         :return:
#         '''
#         data=eval(self.tablename).objects.filter(id=rows)
#         value=data[0]
#         return value




if __name__ == '__main__':
    cc = BaseDB()
    re = cc.get_all_data('select * from Webserver_testcase where casename in ("获取用户手机号","测试")')


    # dd = Testcase.objects.fiter(id='1')
    # # class BaseDBDJ(object):
    # print(dd[0])
