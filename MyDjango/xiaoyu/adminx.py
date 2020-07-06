import xadmin
from . import models

class ControlFileImage(object):
    list_display = ("title", "add_time")


xadmin.site.register(models.FileImage, ControlFileImage)



#一对一关联，注册表
class MoreInfo(object):
    model = models.CardDetail


class ControlCard(object):
    list_display = ("card_id", "card_user", "手机号","城市","add_time")

    #内联显示
    inlines = [MoreInfo]

    def 手机号(self, obj):
        return obj.carddetail.tel

    def 城市(self, obj):
        return obj.carddetail.address


#注册
xadmin.site.register(models.Card, ControlCard)





class ControlPersonInfo(object):
    list_display = ("name", "age", "tel", "mail", "create_time", "update_time")
    list_per_page = 5 #每页最大显示5条、分页
    list_filter = ('tel',)#过滤器
    search_fields = ('tel','mail',"name",)#搜索
    #排序，修改时间,加横岗 - 表示倒序
    ordering = ('-update_time',)
    list_editable = ('mail',)# 快速编辑

xadmin.site.register(models.PersonInfo, ControlPersonInfo)


class ControlStudent(object):
    list_display = ("student_id", "name", "score")
    search_fields = ("student_id", "name")
    list_per_page = 10


xadmin.site.register(models.Student, ControlStudent)
