#编写过滤标签函数
from django import template

register = template.Library()


@register.filter(name="replace")
def myreplace(value, arg):
    return value.replace(arg, "~")
