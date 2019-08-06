from django.db import models


# Create your models here.
class Testcase(models.Model):
    check_result = (
        ('pass', '通过'),
        ('wrong', '不通过'),
    )
    id = models.AutoField(primary_key=True, blank=False, verbose_name='案例编号')
    casename = models.CharField(max_length=30, blank=False, verbose_name='测试用例名称')
    frontsql = models.CharField(max_length=200, blank=True, verbose_name='前置SQL')
    apipath = models.CharField(max_length=50, blank=False, verbose_name='接口路径')
    requestmethod = models.CharField(max_length=20, blank=False, verbose_name='请求方法')
    requestdata = models.CharField(max_length=200, blank=False, verbose_name='接口请求数据')
    httpcodecheck = models.CharField(max_length=20, blank=True, verbose_name='HTTPcode检查点')
    responsecode = models.CharField(max_length=20, blank=True, verbose_name='实际返回码')
    result = models.CharField(max_length=5, choices=check_result,blank=True, verbose_name='比对结果')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name

        def __str__(self):  # __str__ 方法是把  QuerySet 的方法显示具体的名称
            return self.verbose_name
