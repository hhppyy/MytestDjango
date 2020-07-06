from django.db import models


# Create your models here.

#上传文件和图片
class FileImage(models.Model):
    '''文件和图片'''
    title = models.CharField(max_length=30,
                             blank=True,
                             null=True,
                             verbose_name="标题名称")
    image = models.ImageField(blank=True,
                             null=True,
                              upload_to="up_image",
                             verbose_name="图片")
    file = models.FileField(blank=True,
                             null=True,
                            upload_to="up_file",
                             verbose_name="文件")

    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name="创建时间")

    class Meta:
        verbose_name_plural = "文件和图片"
        verbose_name = "文件和图片"

    def __str__(self):
        return self.title


#表关联，一对一
class Card(models.Model):
    '''银行卡'''
    card_id = models.CharField(verbose_name="银行卡号",
                               max_length=30)
    card_user = models.CharField(verbose_name="持卡人",
                                 max_length=30)

    add_time = models.DateTimeField(auto_now=True,
                                    verbose_name="创建时间")

    class Meta:
        verbose_name_plural = "银行卡"
        verbose_name = "银行卡"

    def __str__(self):
        return self.card_id


class CardDetail(models.Model):
    '''银行卡详情'''
    card = models.OneToOneField(Card,
                                on_delete=models.CASCADE,
                                verbose_name="银行卡号")

    tel = models.CharField(verbose_name="持卡人手机号",
                           max_length=30,
                           blank=True,
                           null=True,
                           default="")

    mail = models.CharField(verbose_name="邮箱",
                            max_length=30,
                            blank=True,
                            null=True,
                            default="")

    city = models.CharField(verbose_name="城市",
                            max_length=30,
                            blank=True,
                            null=True,
                            default="")

    address = models.CharField(verbose_name="地址",
                               blank=True,
                               null=True,
                               max_length=100,
                               default="")

    class Meta:
        verbose_name_plural = "银行卡详情"
        verbose_name = "银行卡详情"

    def __str__(self):
        return self.card.card_user


class Student(models.Model):
    '''学生成绩单'''
    student_id = models.CharField(verbose_name="学号",
                                  max_length=30,
                                  null=True,
                                  blank=True)
    name = models.CharField(verbose_name="姓名",
                            max_length=30,
                            null=True,
                            blank=True)
    score = models.IntegerField(verbose_name="分数",
                                null=True,
                                blank=True)

    class Meta:
        verbose_name_plural = "学生成绩单"






# 新建一个PersonInfo类，继承自models.Model
class PersonInfo(models.Model):
    '''个人信息'''
    name = models.CharField(verbose_name="名称", max_length=30, null=True, blank=True)
    # name字段，字符串类型(必须要有长度max_length)，长度30，可以为空，可以为null
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True)
    # age字段，int类型，可以为null
    # 整数列(有符号的) -2147483648 ～ 2147483647
    mail = models.EmailField(verbose_name="邮箱", default='123@qq.com')
    # mail字段，默认值为123@qq.com
    tel = models.BigIntegerField(verbose_name="电话", null=True,blank=True)
    # 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True,null=True, blank=True)
    #创建时间为系统时间
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True,null=True, blank=True)
    #修改时间为系统时间
    def __str__(self):
        return self.__doc__ + ':' + self.name

    class Meta:
        verbose_name_plural = "个人信息"


# 新建一个PersonInfoNew类，继承自models.Model
class PersonInfoNew(models.Model):
    uid = models.IntegerField(primary_key=True)
    # uid字段，int类型，主键
    name = models.CharField(max_length=30, null=True, blank=True)
    # name字段，字符串类型，长度30，可以为空，可以为null
    age = models.IntegerField(null=True, blank=True)
    # age字段，int类型，可以为null,可以为空

    text = models.TextField(null=True,blank=True)
    #文本类型
    img = models.ImageField(default='')
    #图片类型
    file = models.FileField(default='')
    #文件类型
    b = models.BooleanField(default='True')
    #布尔值，True ，Fales

    date = models.DateField(null=True, blank=True)
    #日期 2020-06-20
    time = models.TimeField(null=True, blank=True)
    #时间 21:22:02
    date_time = models.DateTimeField(null=True, blank=True)
    #日期加时间 2020-06-20 21:22:02

