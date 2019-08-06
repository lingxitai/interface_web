import pytest
# pip install -U pytest,pip install -U pytest-html
from base.getCase import GetCase
from base.baseHttp import BaseHttp
from base.log import Log
import json
from base.baseDB import BaseDB

# @pytest.mark.parametrize('a,b,result', [(1, 2, 3), (2, 2, 3), (5, 5, 10)])
# def test_1(a, b, result):
#     assert a + b == result


Getlog = Log('test_Run')
getlog = Getlog.log()
getcase = GetCase()
case_data = getcase.get_case_data()
getlog.info('获取案例为：\n {0}'.format(case_data))
basehttp = BaseHttp()
basedb = BaseDB()

'''
前面参数是具体一个case_data，后面参数是由case组成的列表
'''


@pytest.mark.parametrize('case_data', case_data)
def test_1(case_data):
    getlog.info('-----------案例名称为：{0}--开始执行-------------'.format(case_data['测试用例']))
    if case_data['请求方法'] == 'post':
        response = basehttp.post(case_data['接口路径'], case_data['请求体'])
        js_response = json.loads(response.content)
        getlog.info(
            '案例：{0}的response.content转为字典{1},最终返回码为{2}'.format(case_data['测试用例'], js_response, js_response['code']))
        try:  # 将返回码回插库中，方便查看
            basedb.excutesql(
                'update Webserver_testcase set responsecode="{1}" where casename = "{0}"  '.format(case_data['测试用例'],
                                                                                                   js_response['code']))
        except Exception as e:
            getlog.error('----{0}-----案例插库返回码错误，具体为：{1}'.format(case_data['测试用例'], e))


    elif case_data['请求方法'] == 'get':
        response = basehttp.get(case_data['接口路径'], case_data['请求体'])
        js_response = json.loads(response.content)
        getlog.info(
            '案例：{0}的response.content转为字典{1},最终返回码为{2}'.format(case_data['测试用例'], js_response, js_response['code']))
        try:  # 将返回码回插库中，方便查看
            basedb.excutesql(
                'update Webserver_testcase set responsecode="{1}" where casename = "{0}"  '.format(case_data['测试用例'],
                                                                                                   js_response['code']))
        except Exception as e:
            getlog.error('----{0}-----案例插库返回码错误，具体为：{1}'.format(case_data['测试用例'], e))
    elif case_data['请求方法'] == 'post_with_json':
        response = basehttp.post_with_json(case_data['接口路径'], case_data['请求体'])
        js_response = json.loads(response.content)
        getlog.info(
            '案例：{0}的response.content转为字典{1},最终返回码为{2}'.format(case_data['测试用例'], js_response, js_response['code']))
        try:  # 将返回码回插库中，方便查看
            basedb.excutesql(
                'update Webserver_testcase set responsecode="{1}" where casename = "{0}"  '.format(case_data['测试用例'],
                                                                                                   js_response['code']))
        except Exception as e:
            getlog.error('----{0}-----案例插库返回码错误，具体为：{1}'.format(case_data['测试用例'], e))
    assert (js_response['code']) == int(case_data['HttpCode'])


if __name__ == '__main__':
    pytest.main()
