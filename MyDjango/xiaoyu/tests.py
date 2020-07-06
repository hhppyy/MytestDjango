from django.test import TestCase

# Create your tests here.


class Person():
    '''人类'''
    name = 'han'
    age = 20
    mail = '123@qq.com'

    def __str__(self):
        '''描述对象'''
        return self.__doc__

a = Person() #a是object对象
print(a)# <__main__.Person object at 0x00000000028CA390>

