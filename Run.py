import os
import operationConfig as opconfig
import time
from base.log import Log
# file=os.popen('pip freeze >>requirment.txt')
# # file.read()
# os.system('pip freeze >>requirment1.txt')


config=opconfig.CONFIG()
report_dir=os.path.join(opconfig.PROJECT_DIR,'report\{0}'.format(time.strftime('%Y%m%d')))
# print(report_dir)
config.set_config_value('REPORT','path',report_dir)
report_dir=config.get_config_value('REPORT','path')
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
Getlog=Log('Run')
getlog=Getlog.log()
getlog.info('报告和日志文件父路径创建成功')
# file=os.popen('pytest Runcode --html={0}/测试报告.html'.format(report_dir))
# file.read()#此方法有时会有乱码，因编码问题不能read()
os.system('pytest Runcode --html={0}/测试报告.html'.format(report_dir))
getlog.info('案例执行完，请查看（{0}）测试报告'.format(report_dir))
