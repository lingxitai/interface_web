from base.log import Log
from operationConfig import CONFIG
import requests


class BaseHttp():
    '''
    封装get post post_with_json 三种方式，用于获取response
    '''
    GetLog = Log('basehttp')
    getlog = GetLog.log()
    getconfig = CONFIG()
    scheme = getconfig.get_config_value('HTTP', 'scheme')
    baseurl = getconfig.get_config_value('HTTP', 'baseurl')
    port = getconfig.get_config_value('HTTP', 'port')
    timeout = getconfig.get_config_value('HTTP', 'timeout')
    if port:
        baseurl = scheme + ':' + '//' + baseurl + ':' + port
        getlog.info('有端口号拼接地址为：{0}'.format(baseurl))
    else:
        baseurl = scheme + ':' + '//' + baseurl
        getlog.info('无端口号拼接地址为：{0}'.format(baseurl))

    def get(self,uri,params):
        headers={'Content-type': 'application/x-www-form-urlencoded'}
        url=self.baseurl+uri
        self.getlog.info('最终拼接地址为：{0}'.format(url))
        try:
            response=requests.get(headers=headers,url=url,params=params)
            self.getlog.info('get请求成功，返回结果为：{0}'.format(response))

        except TimeoutError as e:
            self.getlog.erro('get请求失败，报错为：{0}'.format(e))
        return response
    def post(self,uri,params):
        headers={'Content-type': 'application/x-www-form-urlencoded'}
        url=self.baseurl+uri
        self.getlog.info('最终拼接地址为：{0}'.format(url))
        try:
            response=requests.post(headers=headers,url=url,params=params,timeout=int(self.timeout))
            self.getlog.info('post请求成功，返回结果为：{0}'.format(response))

        except TimeoutError as e:
            self.getlog.erro('post请求失败，报错为：{0}'.format(e))
        return response

    def post_with_json(self,uri,params):
        headers={'Content-type': 'application/json'}
        url=self.baseurl+uri
        self.getlog.info('最终拼接地址为：{0}'.format(url))
        try:
            response=requests.post(headers=headers,url=url,json=params)
            self.getlog.info('post_with_json请求成功，返回结果为：{0}'.format(response))

        except TimeoutError as e:
            self.getlog.erro('post_with_json请求失败，报错为：{0}'.format(e))
        return response



if __name__ == ('__main__'):
    # cc = BaseHttp()
    # bas = cc.post('/web',{'query':'杨幂'})
    # print(bas)
    cc = BaseHttp()
    bas = cc.post_with_json('/web',{'query':'杨幂'})
    print(bas)
