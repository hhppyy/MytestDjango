from django.contrib import admin
from .import models

# Register your models here.
admin.site.site_header = 'xiaoyu项目管理系统'
admin.site.site_title = '登录xiaoyu系统后台'
admin.site.index_title = 'xiaoyu后台管理'



@admin.register(models.PersonInfo)
class ControlPersonInfo(admin.ModelAdmin):
    list_display = ("name", "age", "tel", "mail", "create_time", "update_time")
    list_per_page = 5 #每页最大显示5条、分页
    list_filter = ('tel',)#过滤器
    search_fields = ('tel','mail',"name",)#搜索
    #排序，修改时间,加横岗 - 表示倒序
    ordering = ('-update_time',)
    list_editable = ('mail',)# 快速编辑


# admin.site.register(models.PersonInfo, ControlPersonInfo) #注册模型


