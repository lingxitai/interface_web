from django.shortcuts import render
from django.shortcuts import HttpResponse
import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interface_web.settings")# project_name 项目名称
# django.setup()
# Create your views here.
# from Webserver.models import Testcase
# dd = Testcase.objects.fiter(id='1')
# # # class BaseDBDJ(object):
# # print(dd[0])
# case_data = Testcase.objects.filter(casename='获取用户手机号')
# case = case_data[0]
# print(case.apipath)
from base import baseDB
# a=baseDB.DJ_basedb('Testcase')
# aa=a.getdj_one_date(1)
# def test(request):
#     # case_data=Testcase.objects.filter(casename='获取用户手机号')
#     # case=case_data[0]
#     # list1=[]
#     # case_data=Testcase.objects.all()
#     # for i in aa:
#     #     list1.append(i.apipath)
#     return HttpResponse("你好？{0}".format(aa.apipath))
