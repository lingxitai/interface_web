from django.contrib import admin

# Register your models here.
from .models import Testcase

admin.site.site_header='接口测试管理系统简易版'
admin.site.site_title='接口测试'

class TestcaseAdmin(admin.ModelAdmin):
    list_display=['id','casename','frontsql','apipath','requestmethod','requestdata','httpcodecheck','responsecode','result','create_time']

admin.site.register(Testcase,TestcaseAdmin)