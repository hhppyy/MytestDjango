# Generated by Django 2.0.3 on 2020-06-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaoyu', '0004_personinfonew'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='mail',
            field=models.EmailField(default='123@qq.com', max_length=254),
        ),
    ]
